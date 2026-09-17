# AGENTS.md — AI Developer & Collaborator Guide

> **Project:** Miniature Kolsky (Split-Hopkinson Pressure) Bar & Abaqus Digital Twin Research Poster  
> **Institutions:** The Pennsylvania State University & Los Alamos National Laboratory (LANL)  
> **Physical Poster Dimensions:** 24 in $\times$ 32 in (Portrait) / 609.6 mm $\times$ 812.8 mm  
> **Primary Maintainer:** Reuben H. Kraft (Penn State)

---

## 1. Executive Summary & Purpose

This repository houses the design, scientific narrative, figures, and build pipelines for a 24" $\times$ 32" research poster showcasing the synergy between **Miniature Kolsky Bar experiments** ($\varnothing 3.17\,\text{mm}$) and an **Abaqus Explicit Digital Twin** for high-strain-rate material characterization ($10^3\text{ to }10^5\,\text{s}^{-1}$).

The project maintains two parallel, synchronized implementations:
1. **HTML/CSS Poster (`html/`)**: *Primary recommendation* for flexible typography, rapid visual iteration, and pixel-perfect printing via headless Chromium.
2. **LaTeX/TikZ Poster (`latex/`)**: Traditional academic print workflow using `beamerposter` / `tikz`.

Future AI tools and contributors must consult this guide to understand design decisions, repository architecture, figure generation scripts, and exact compilation workflows before making changes.

---

## 2. Scientific & Narrative Framework

The central theme emphasized throughout the poster is **the tight coupling of Computation and Experiment**:
- Computation is **not** an afterthought; the **Abaqus Digital Twin** models the full 3D bar-specimen assembly to validate stress wave propagation, correct for inertial and frictional dispersion, and design tailored pulse shapers.
- Experiments provide high-fidelity dynamic strain gage data, ultra-high-speed imaging, and in-situ DIC to calibrate and validate strain-rate-dependent constitutive models (e.g., Johnson-Cook, Zerilli-Armstrong).
- The narrative culminates in a forward-looking vision for an **Autonomous High-Throughput Facility** capable of ~1,000 dynamic tests per day via robotics, automated pulse shaping, and Bayesian active learning.

### Section & Card Architecture (2 Columns $\times$ 3 Rows + Central Ribbon)

| Element | Location | Content & Technical Focus | Key Visual Assets |
| :--- | :--- | :--- | :--- |
| **Header** | Top Banner | Title highlighting Experimental & Computational Digital Twin synergy; PSU & LANL logos; Authors (Reuben H. Kraft at end). | `images/psu_logo.png`, `images/lanl_logo.png` |
| **Card 1** | Col 1, Row 1 | **Experimental Facility — Miniature Kolsky Bar ($\varnothing 3.17\,\text{mm}$)**<br>Maraging 350 steel bars, striker launcher, laser vibrometer alignment, high-frequency strain gages ($10^3 - 10^5\,\text{s}^{-1}$). | CAD render / photograph of mini-bar assembly. |
| **Card 2** | Col 2, Row 1 | **Computational Digital Twin — Abaqus Explicit 3D**<br>Full bar-specimen FE mesh, dynamic wave propagation modeling, contact algorithms, virtual stress-equilibrium verification. | `images/digital_twin_card.png` (Full bar mesh + zoomed specimen callout). |
| **Workflow Ribbon** | Full-width between Row 1 & 2 | **Integrated Synergy Workflow**<br>Circular feedback: Physical Shot $\leftrightarrow$ Pulse Shaper $\leftrightarrow$ Digital Twin $\leftrightarrow$ Constitutive Library. | Flow diagram / pill-badge sequence. |
| **Card 3** | Col 1, Row 2 | **Innovative Pulse Shaping for Tailored Dynamic Response**<br>Annealed copper/polymer shapers to ramp incident pulses, eliminate Pochhammer-Chree high-frequency oscillations, and ensure constant $\dot{\varepsilon}$. | Comparison plots of raw vs. shaped wave profiles & dynamic equilibrium ($F_1 \approx F_2$). |
| **Card 4** | Col 2, Row 2 | **Ultra-High-Speed Imaging & In-Situ Full-Field DIC**<br>Shimadzu / Kirana high-speed imaging (up to $5\,\text{MHz}$), tracking plastic localization, shear band formation, and micro-cracking. | `images/imaging_strip.png` (High-speed deformation sequence). |
| **Card 5** | Col 1, Row 3 | **Dynamic Constitutive Response Across Strain Rates**<br>Single consolidated rate-dependent flow stress curve ($10^{-3}$ to $10^4\,\text{s}^{-1}$), hardening parameters, temperature/strain-rate sensitivity. | Consolidated stress-strain curve + JC parameter table. |
| **Card 6** | Col 2, Row 3 | **Vision: Autonomous High-Throughput Facility ("What We Could Do")**<br>Roadmap toward 1,000 tests/day: automated robotic loading, computer vision alignment, closed-loop Bayesian optimization. | `images/automation_concept.png` (5-stage linear pipeline + localized feedback loop). |

---

## 3. Style Guide & Design Rules

To preserve visual hierarchy and institutional polish, all edits **must** adhere to these constraints:

### A. Color Palette
- **Institutional Navy (Primary Dark):** `#0B2545` (Headers, title, card accents)
- **Mid/Tech Blue (Secondary Accent):** `#1F4E8C` (Sub-headers, table borders, key indicators)
- **LANL/PSU Gold Accent:** `#D49B28` or `#C88A1A` (Metrics callouts, active learning badge, highlights)
- **Ice / Off-White Tint:** `#F0F5FA` or `#F4F7FB` (Card body backgrounds, subtle badges)
- **Card Backgrounds:** `#FFFFFF` (High contrast, crisp text rendering)
- **Text Color:** `#1A202C` (Deep charcoal, never pure `#000000` for body copy)

### B. Header & Logo Alignment Rules
- **Pure White Background (`#FFFFFF`):** The header banner **must** have a clean white background. Both the Penn State and LANL institutional logos contain white bounding boxes; placing them on colored banners produces unsightly rectangular borders.
- **Author Ordering:** Reuben H. Kraft **must be listed at the end** of the author list.
- **Sponsorship / Task Order Notice:** Omit explicit contract task orders or sponsorship disclaimers from the top banner to maximize visual space for the scientific title.

### C. Grid Alignment & Fill Factor
- **Strict Row Alignment:** Row 1 (Cards 1 & 2), Row 2 (Cards 3 & 4), and Row 3 (Cards 5 & 6) must align their top and bottom bounding boxes exactly. Col 1 and Col 2 must be identically sized ($27.5\,\text{cm}$ in LaTeX, `1fr 1fr` in CSS).
- **High Fill Factor / Zero Dead Space:** Fill card bodies completely with large graphics, concise multi-column callouts, and key data points. Minimize empty white margins inside cards.

---

## 4. Repository Structure & Directory Map

```text
SHPB_Poster/
├── AGENTS.md                      # THIS FILE — Primary instructions for AI agents
├── README.md                      # Quick-start guide for human users
├── final_report_text.txt          # Background technical report & project source text
│
├── html/                          # MODERN HTML/CSS POSTER PIPELINE
│   ├── poster.html                # Master HTML/CSS poster source
│   ├── Kolsky_Poster_HTML.pdf     # Vector PDF output (24" x 32", 300 DPI target)
│   ├── poster_html_preview-1.png  # Rendered preview image for verification
│   └── images -> ../images        # NTFS Directory Junction to shared images
│
├── latex/                         # LATEX/TIKZ POSTER PIPELINE
│   ├── main.tex                   # Master LaTeX beamerposter source
│   ├── Kolsky_Poster_LaTeX.pdf    # Compiled LaTeX PDF output
│   ├── poster_updated_preview-1.png # Rendered preview image of LaTeX version
│   └── images -> ../images        # NTFS Directory Junction to shared images
│
├── images/                        # MASTER SHARED ASSET DIRECTORY
│   ├── psu_logo.png               # Penn State mark
│   ├── lanl_logo.png              # Los Alamos mark
│   ├── automation_concept.png     # 5-stage automated testing + Bayesian loop diagram
│   ├── digital_twin_card.png      # Abaqus 3D mesh composite figure
│   ├── imaging_strip.png          # High-speed DIC sequence composite
│   └── [data plots / micrographs]
│
└── scripts/                       # ASSET GENERATION & COMPOSITING SCRIPTS
    ├── generate_automation_diagram.py # Creates images/automation_concept.png
    ├── generate_digital_twin.py       # Creates images/digital_twin_card.png
    ├── generate_imaging_strip.py      # Creates images/imaging_strip.png
    └── generate_card5_composite.py    # Creates rate-dependent flow stress plots
```

> [!IMPORTANT]
> **Disk Space & Junction Links:** Do **not** copy the `images/` directory into `html/` or `latex/`. Both subfolders use NTFS Directory Junctions (`mklink /J` or `New-Item -ItemType Junction`) pointing to the root `images/` folder to prevent duplicating >100 MB of assets.

---

## 5. Build, Compilation & Verification Procedures

All commands are executed from the repository root in **Windows PowerShell**:

### 1. Recompiling the HTML/CSS Poster to PDF
We use headless Google Chrome with modern print flags. Always pass `--user-data-dir` to an isolated directory so it executes cleanly even when Chrome is already running:

```powershell
Start-Process -FilePath "chrome.exe" -ArgumentList `
  '--headless=new', `
  '--no-pdf-header-footer', `
  '--run-all-compositor-stages-before-draw', `
  '--user-data-dir="C:\Users\reube\AppData\Local\Temp\chrome_poster_build"', `
  '--print-to-pdf="C:\Users\reube\BeeStation\PSU-OneDrive-08-16-2026\research\lanl\SHPB_Poster\html\Kolsky_Poster_HTML.pdf"', `
  ('file:///' + ((Resolve-Path "html\poster.html").Path -replace '\\', '/')) `
  -Wait -NoNewWindow
```

### 2. Rendering PDF Previews to PNG for Agent Inspection
Use `pdftoppm` (from Poppler / MiKTeX) to generate high-resolution PNG previews:

```powershell
pdftoppm -png -r 150 html\Kolsky_Poster_HTML.pdf html\poster_html_preview
# Produces html\poster_html_preview-1.png
```

Inspect the rendered image with `view_file` to verify formatting, layout alignment, and typography.

### 3. Compiling the LaTeX Poster
Run `pdflatex` inside the `latex/` directory:

```powershell
cd latex
pdflatex -jobname=Kolsky_Poster_LaTeX -interaction=nonstopmode main.tex
cd ..
```

Render LaTeX preview:
```powershell
pdftoppm -png -r 150 latex\Kolsky_Poster_LaTeX.pdf latex\poster_updated_preview
```

### 4. Regenerating Python Figures
When modifying diagrams or plots:
```powershell
python scripts/generate_automation_diagram.py
python scripts/generate_digital_twin.py
python scripts/generate_imaging_strip.py
python scripts/generate_card5_composite.py
```
*Note: Generated images automatically save directly into `images/` and instantly propagate to both `html/` and `latex/` via junctions.*

---

## 6. Notable Bug Fixes & Design History

1. **Automation Graphic Feedback Arc (`images/automation_concept.png`):**
   - *Issue:* A long, sweeping dotted line originally spanned the entire width of the diagram from the active learning badge back to stage 1, cutting awkwardly across the bottom of stages 2, 3, and 4.
   - *Resolution:* Fixed in `scripts/generate_automation_diagram.py`. The long arc was removed and replaced with clean, localized vertical connectors with discrete pill badges (`"Uncertainty Feedback"` $\downarrow$ and `"Next Test Command"` $\uparrow$).
2. **Institutional Logo Background Clash:**
   - *Issue:* Dark or blue header bars created glaring white boxes around university and laboratory logos.
   - *Resolution:* Switched the main header background to pure `#FFFFFF` with navy text and dark sub-bars.
3. **Card Grid Disalignment:**
   - *Issue:* Uneven text lengths previously caused the bottom borders of Cards 1 and 2 to diverge.
   - *Resolution:* Locked both HTML and LaTeX layouts to rigid 2-column grid geometry with matched heights and standardized image sizes.
4. **Author Sequence:**
   - Reuben H. Kraft placed at the conclusion of the author line.

---

## 7. Directives for Future AI Agents

When tasked with further modifications:
1. **Preserve Synchronicity:** If updating text, data, or figures, ensure both `html/poster.html` and `latex/main.tex` are updated or notify the user of the primary target.
2. **Verify Visually:** Always re-run the headless Chrome build and `pdftoppm` command, then call `view_file` on the resulting PNG to verify margins, word wrapping, and alignment before declaring task completion.
3. **No File Bloat:** Store one-off scratch scripts in the designated scratch directory; never dump uncompressed duplicate image folders into the repository.
