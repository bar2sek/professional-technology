---
title: "Professional Resume & Platform Engineering Portfolio"
date: 2026-09-07
tags:
  - resume
  - career
  - aws
  - terraform
  - python
  - hub
status: evergreen
aliases:
  - "Resume Hub"
  - "Career Portfolio"
---

# Ryan Bartusek – Resume & Platform Engineering Portfolio

[![AWS Certified](https://img.shields.io/badge/AWS-Certified-orange.svg)](https://aws.amazon.com)
[![Aviatrix ACE](https://img.shields.io/badge/Aviatrix-ACE%20Multicloud-purple.svg)](https://aviatrix.com)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-blue.svg)](https://www.terraform.io)
[![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)

**Ryan Bartusek**  
*Enterprise Cloud Architecture | Cloud Platform Engineering*  
Des Moines, IA • [LinkedIn](https://linkedin.com/in/bar2sek) • [GitHub](https://github.com/bar2sek)

---

## Overview

This directory maintains the iterative source, formatting, and automated generation pipeline for Ryan Bartusek's professional resume, co-located within the `professional-technology` repository. 

It implements a **dual-artifact workflow**:
1. **Semantic Markdown (`.md`)**: Human-readable, ATS-friendly plain-text drafts optimized for git diffing, version control, and text intake systems.
2. **Headless PDF Engine (`render_pdf.py` + Chrome/Brave)**: Parses the Markdown, applies a print stylesheet, and prints a vector PDF through headless Chromium (Google Chrome or Brave Browser).

> [!IMPORTANT] The Markdown is the single source of truth
> All content edits go in the `.md` file. `render_pdf.py` holds only the parser and the stylesheet, never resume content, so the Markdown and the PDF can't drift apart.

> [!NOTE] No length limit
> The layout is tuned for readability (10pt body text, generous margins and spacing), not for fitting a page count. The resume runs as many pages as the content needs; page breaks keep each role's heading with its first bullet.

---

## Directory Structure

```text
resume/
├── Ryan_Bartusek_Resume_2026v8.md   # Current resume content (single source of truth)
├── Ryan_Bartusek_Resume_2026v8.pdf  # Generated PDF
├── render_pdf.py                    # Markdown parser + print stylesheet + headless Chrome call
├── Ryan_Bartusek_Resume_2026v5-v7.* # Historical versions
└── README.md                        # This file
```

---

## PDF Generation Pipeline

The resume PDF is built using `render_pdf.py`, which generates a temporary HTML preview with embedded print styles and runs headless Chromium (Brave Browser or Google Chrome) to print the layout to a crisp vector PDF.

### Prerequisites

- **Python 3.8+**
- **Chromium-based Browser** (Google Chrome or Brave Browser):
  - macOS auto-detected: `/Applications/Brave Browser.app` or `/Applications/Google Chrome.app`
  - Linux/Other: Standard `google-chrome`, `brave-browser`, or `chromium` binary in `PATH`
  - Can also be explicitly specified via the `CHROME_PATH` environment variable (e.g. `export CHROME_PATH="/path/to/chrome"`)

### Building the PDF

```bash
python3 render_pdf.py                                 # newest Ryan_Bartusek_Resume_*vN.md
```

```bash
python3 render_pdf.py Ryan_Bartusek_Resume_2026v8.md  # a specific version
```

The script uses only the Python standard library. On each run it:
1. Parses the Markdown (see the docstring at the top of `render_pdf.py` for the expected shape).
2. Writes the styled HTML to `resume_preview.html` (gitignored; open it in a browser to check the layout).
3. Runs headless Chromium with a throwaway profile and prints to PDF with no headers or footers.
4. Writes the PDF next to the source with the same name (`…v8.md` → `…v8.pdf`).

### Starting a new version

Copy the latest `.md` to the next version number, edit the copy, and run the script; it picks up the newest version automatically.

### Gotchas

- **Keep the Markdown shape.** Job entries need `### Company` followed by `**Title** | *Dates*`; projects use `### Name` followed by an italic `*tech · stack*` line. Anything else renders as a plain paragraph.
- **Earlier Experience, Education and Certifications** render as compact lists; the section names are listed in `COMPACT_SECTIONS` in the script.
- **Check the page breaks after big edits.** Open the PDF; if a heading looks stranded, it's a stylesheet issue, not a content one.

---

## Iteration History

| Version | Status | Key Highlights |
|---|---|---|
| **v8** | **Active** | Accuracy pass (Bedrock, migration, Azure landing zones, Principal), plain-language summary, de-duplicated skills, Projects section (homelab, Bedrock AI Gateway), GitHub link; readable multi-page layout rendered from Markdown. |
| **v7** | Archived | Refined typography, updated enterprise cloud initiatives (AFT, Amazon Bedrock, Amazon Connect, Aviatrix), single-page letter fitting. |
| **v6** | Archived | Cloud Infrastructure Team Lead promotion updates, multi-account topology framing. |
| **v5** | Archived | Initial 2026 revision baseline. |

---

## Git & Tracking Policy

- **Source Files (`*.md`, `*.py`)**: Tracked in version control.
- **Compiled PDFs (`*.pdf`)**: Tracked to allow direct downloads and release tagging.
- **Build Artifacts & Profiles (`.chrome_profile/`, `resume_preview.html`, `__pycache__/`)**: Ignored via [`.gitignore`](.gitignore).
