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
Des Moines, IA • [bar2sek@users.noreply.github.com](mailto:bar2sek@users.noreply.github.com) • [LinkedIn](https://linkedin.com/in/bar2sek)

---

## Overview

This directory maintains the iterative source, formatting, and automated generation pipeline for Ryan Bartusek's professional resume, co-located within the `professional-technology` repository. 

It implements a **dual-artifact workflow**:
1. **Semantic Markdown (`.md`)**: Human-readable, ATS-friendly plain-text drafts optimized for git diffing, version control, and text intake systems.
2. **Programmatic Headless PDF Engine (`.py` + Chrome/Brave)**: Single-page, pixel-perfect print layout rendered via headless Chromium (Google Chrome or Brave Browser) with fine-tuned CSS print media rules (`@page`, exact leading, vector typography, and compact margins).

---

## Directory Structure

```text
resume/
├── Ryan_Bartusek_Resume_2026v7.md   # Current active resume content (Markdown)
├── Ryan_Bartusek_Resume_2026v7.pdf  # Compiled, print-ready PDF output
├── render_pdf.py                    # Python script & embedded CSS template to build PDF
├── Ryan_Bartusek_Resume_2026v6.md   # Historical v6 markdown source
├── Ryan_Bartusek_Resume_2026v6.pdf  # Historical v6 PDF output
├── Ryan_Bartusek_Resume_2026v5.md   # Historical v5 markdown source
└── README.md                        # Portfolio documentation
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

To compile the latest version of the resume into PDF format:

```bash
python3 render_pdf.py
```

Upon execution, the script:
1. Emits the styled HTML layout to `resume_preview.html`.
2. Spins up a headless Chromium process (Google Chrome or Brave Browser).
3. Prints to PDF without headers/footers (`--no-pdf-header-footer`) using letter size (`margin: 0.42in 0.48in`).
4. Outputs the target PDF (e.g., `Ryan_Bartusek_Resume_2026v7.pdf`).

---

## Iteration History

| Version | Status | Key Highlights |
|---|---|---|
| **v7** | **Active** | Refined typography, balanced section spacing, updated enterprise cloud initiatives (AFT, Amazon Bedrock, Amazon Connect, Aviatrix), and single-page letter fitting. |
| **v6** | Archived | Cloud Infrastructure Team Lead promotion updates, multi-account topology framing. |
| **v5** | Archived | Initial 2026 revision baseline. |

---

## Git & Tracking Policy

- **Source Files (`*.md`, `*.py`)**: Tracked in version control.
- **Compiled PDFs (`*.pdf`)**: Tracked to allow direct downloads and release tagging.
- **Build Artifacts & Profiles (`.chrome_profile/`, `resume_preview.html`, `__pycache__/`)**: Ignored via [`.gitignore`](.gitignore).
