"""Render the resume Markdown into a print-ready PDF via headless Chromium.

The Markdown file is the single source of truth: this script parses it,
wraps it in the stylesheet below, and prints it to PDF. Content edits go in
the .md only.

Usage:
    python3 render_pdf.py                                 # newest Ryan_Bartusek_Resume_*vN.md
    python3 render_pdf.py Ryan_Bartusek_Resume_2026v8.md  # a specific version

Expected Markdown shape (stdlib parser, no dependencies):
    # Name
    ### Subtitle
    Contact line | with | links
    ## Section
    ### Entry heading (company or project)
    **Job Title** | *Dates*      <- title row, dates right-aligned
    *Tech · stack · line*        <- italic-only line under an entry
    - Bullet with **bold**, *italic* and [links](url)
    Lines of `---` are ignored; spacing comes from the stylesheet.
"""

import glob
import html
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

# Sections rendered as compact lists rather than full entries.
COMPACT_SECTIONS = {"Earlier Experience", "Education", "Certifications"}

CSS = """
  @page {
    size: letter;
    margin: 0.6in 0.7in;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 10pt;
    line-height: 1.4;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  a { color: inherit; text-decoration: none; }
  strong { color: #0f172a; font-weight: 700; }

  /* Header */
  .header {
    text-align: center;
    border-bottom: 2px solid #0f172a;
    padding-bottom: 10px;
    margin-bottom: 18px;
  }
  .header h1 {
    font-size: 24pt;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #0f172a;
    text-transform: uppercase;
    margin-bottom: 2px;
  }
  .header .subtitle {
    font-size: 11.5pt;
    font-weight: 700;
    color: #2563eb;
    margin-bottom: 6px;
  }
  .header .contact { font-size: 9.5pt; color: #475569; }
  .header .contact .sep { color: #cbd5e1; margin: 0 8px; }

  /* Sections */
  .section { margin-bottom: 16px; }
  .section-title {
    font-size: 11.5pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    color: #0f172a;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 3px;
    margin-bottom: 10px;
    break-after: avoid;
  }
  .section > p { color: #334155; margin-bottom: 8px; }
  .section > p:last-child { margin-bottom: 0; }

  /* Entries: jobs and projects */
  .entry { margin-bottom: 14px; }
  /* Keeps an entry's heading on the same page as its first bullet. */
  .keep { break-inside: avoid; }
  .entry:last-child { margin-bottom: 0; }
  .entry-head { margin-bottom: 6px; }
  ul.lead + ul li:first-child { margin-top: 0; }
  ul.lead li { margin-bottom: 4px; }
  .entry-name { font-size: 11pt; font-weight: 800; color: #0f172a; }
  .entry-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 16px;
  }
  .entry-title { font-weight: 700; color: #2563eb; }
  .entry-dates { font-size: 9.5pt; font-weight: 600; color: #64748b; white-space: nowrap; }
  .entry-meta { font-size: 9.5pt; color: #64748b; font-style: italic; }
  .entry-meta em { font-style: italic; }
  .project { break-inside: avoid; }

  /* Bullets */
  ul { list-style: none; }
  li {
    position: relative;
    padding-left: 14px;
    margin-bottom: 4px;
    color: #334155;
    break-inside: avoid;
  }
  li::before {
    content: "\\2022";
    position: absolute;
    left: 0;
    color: #0284c7;
    font-weight: bold;
  }
  .compact li { margin-bottom: 3px; }
  .compact li::before { content: "\\25AA"; color: #64748b; font-size: 8.5pt; top: 1px; }
  .section.compact { break-inside: avoid; }
"""


def inline(text):
    """Convert inline Markdown (links, bold, italic) to HTML."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", out)
    return out


def is_italic_line(line):
    return line.startswith("*") and not line.startswith("**") and line.endswith("*")


def parse(md):
    lines = [l.rstrip() for l in md.splitlines()]
    header = {"name": "", "subtitle": "", "contact": ""}
    sections = []  # [{"title", "items": [...]}]
    current = None  # current section
    entry = None  # current entry inside the section

    def close_list(target):
        if target and target.get("_ul"):
            target["blocks"].append(("ul", target.pop("_ul")))

    for line in lines:
        if not line.strip() or line.strip() == "---":
            continue
        if line.startswith("# "):
            header["name"] = line[2:].strip()
            continue
        if line.startswith("## "):
            close_list(entry)
            close_list(current)
            current = {"title": line[3:].strip(), "blocks": [], "entries": []}
            sections.append(current)
            entry = None
            continue
        if current is None and line.startswith("### "):
            header["subtitle"] = line[4:].strip()
            continue
        if current is None:
            header["contact"] = line.strip()
            continue
        if line.startswith("### "):
            close_list(entry)
            close_list(current)
            entry = {"name": line[4:].strip(), "title": "", "dates": "", "meta": "", "blocks": []}
            current["entries"].append(entry)
            continue
        target = entry or current
        if line.startswith("- "):
            target.setdefault("_ul", []).append(line[2:].strip())
            continue
        close_list(target)
        m = re.match(r"^\*\*(.+?)\*\*\s*\|\s*\*(.+?)\*$", line)
        if entry is not None and m and not entry["title"]:
            entry["title"], entry["dates"] = m.group(1), m.group(2)
        elif entry is not None and is_italic_line(line) and not entry["meta"]:
            entry["meta"] = line[1:-1]
        else:
            target["blocks"].append(("p", line.strip()))
    close_list(entry)
    close_list(current)
    return header, sections


def render_blocks(blocks):
    out = []
    for kind, value in blocks:
        if kind == "p":
            out.append(f"<p>{inline(value)}</p>")
        else:
            items = "".join(f"<li>{inline(v)}</li>" for v in value)
            out.append(f"<ul>{items}</ul>")
    return "\n".join(out)


def render(header, sections):
    contact = '<span class="sep">|</span>'.join(
        f"<span>{inline(part.strip())}</span>" for part in header["contact"].split(" | ")
    )
    body = [
        '<div class="header">',
        f"<h1>{inline(header['name'])}</h1>",
        f'<div class="subtitle">{inline(header["subtitle"])}</div>',
        f'<div class="contact">{contact}</div>',
        "</div>",
    ]
    for sec in sections:
        classes = "section compact" if sec["title"] in COMPACT_SECTIONS else "section"
        body.append(f'<div class="{classes}">')
        body.append(f'<div class="section-title">{inline(sec["title"])}</div>')
        body.append(render_blocks(sec["blocks"]))
        for e in sec["entries"]:
            # Projects have no title/dates row; keep them on one page.
            cls = "entry" if e["title"] else "entry project"
            body.append(f'<div class="{cls}"><div class="keep"><div class="entry-head">')
            body.append(f'<div class="entry-name">{inline(e["name"])}</div>')
            if e["title"]:
                body.append(
                    f'<div class="entry-row"><span class="entry-title">{inline(e["title"])}</span>'
                    f'<span class="entry-dates">{inline(e["dates"])}</span></div>'
                )
            if e["meta"]:
                body.append(f'<div class="entry-meta">{inline(e["meta"])}</div>')
            body.append("</div>")
            blocks = list(e["blocks"])
            if blocks and blocks[0][0] == "ul" and blocks[0][1]:
                # Head + first bullet in one unbreakable wrapper, rest flows after.
                first, rest = blocks[0][1][:1], blocks[0][1][1:]
                body.append(f'<ul class="lead">{"".join(f"<li>{inline(v)}</li>" for v in first)}</ul></div>')
                blocks[0] = ("ul", rest) if rest else None
                blocks = [b for b in blocks if b]
            else:
                body.append("</div>")
            body.append(render_blocks(blocks))
            body.append("</div>")
        body.append("</div>")
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
        f"<title>{html.escape(header['name'])} - Resume</title>\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n" + "\n".join(body) + "\n</body>\n</html>\n"
    )


def latest_source():
    def version(path):
        m = re.search(r"v(\d+)\.md$", path)
        return int(m.group(1)) if m else -1

    candidates = glob.glob(os.path.join(HERE, "Ryan_Bartusek_Resume_*v*.md"))
    if not candidates:
        sys.exit("No Ryan_Bartusek_Resume_*vN.md found.")
    return max(candidates, key=version)


def find_chrome():
    if os.environ.get("CHROME_PATH"):
        return os.environ["CHROME_PATH"]
    for path in (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    ):
        if os.path.exists(path):
            return path
    return (
        shutil.which("google-chrome")
        or shutil.which("chromium")
        or shutil.which("chromium-browser")
        or "google-chrome"
    )


def main():
    source = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else latest_source()
    with open(source, encoding="utf-8") as f:
        header, sections = parse(f.read())

    preview = os.path.join(HERE, "resume_preview.html")
    with open(preview, "w", encoding="utf-8") as f:
        f.write(render(header, sections))

    pdf_output = os.path.splitext(source)[0] + ".pdf"
    # Throwaway profile so headless Chrome never touches the user's real profile.
    temp_profile = tempfile.mkdtemp()
    cmd = [
        find_chrome(),
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        f"--user-data-dir={temp_profile}",
        f"--print-to-pdf={pdf_output}",
        pathlib.Path(preview).as_uri(),
    ]

    print(f"Rendering {os.path.basename(source)} ...")
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if res.returncode == 0:
            print(f"Successfully generated {os.path.basename(pdf_output)}")
        else:
            print(f"Error (code {res.returncode}): {res.stderr}")
    except subprocess.TimeoutExpired:
        print("Error: Rendering timed out.")
    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)


if __name__ == "__main__":
    main()
