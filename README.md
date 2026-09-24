# Miniature Kolsky Bar & Digital Twin Poster Project

High-throughput dynamic material characterization poster for Penn State & Los Alamos National Laboratory.

---

## 📁 Repository Structure

```text
SHPB_Poster/
├── html/                          # Modern HTML/CSS Poster (Recommended)
│   ├── poster.html                # Interactive poster source (open in Chrome / Edge)
│   ├── Kolsky_Poster_HTML.pdf     # High-resolution vector print PDF (24" x 32")
│   ├── poster_html_preview-1.png  # High-resolution PNG preview
│   └── images/                    # Junction link to master images
│
├── latex/                         # LaTeX / TikZ Poster Source
│   ├── main.tex                   # LaTeX poster source code
│   ├── Kolsky_Poster_LaTeX.pdf    # Compiled LaTeX print PDF (24" x 32")
│   ├── poster_updated_preview-1.png # Preview image of LaTeX version
│   └── images/                    # Junction link to master images
│
├── pptx/                          # PowerPoint Poster Pipeline (Penn State MPC Compliant)
│   ├── Kolsky_Poster.pptx         # Native editable PowerPoint file (24" x 32")
│   ├── Kolsky_Poster_PPTX.pdf     # Vector print PDF exported from PowerPoint
│   └── poster_pptx_preview-1.png  # Rendered preview image
│
├── images/                        # Master image assets (SEM, Micro-CT, FE meshes, diagrams)
│
├── scripts/                       # Python data visualization and asset generation scripts
│   ├── generate_automation_diagram.py
│   ├── generate_card5_composite.py
│   ├── generate_digital_twin.py
│   ├── generate_imaging_strip.py
│   ├── generate_pptx_poster.py
│   └── export_pptx_to_pdf.ps1
├── AGENTS.md                      # AI Developer & Collaborator Reference Guide
├── README.md
```

For AI agents and developers working on this project, consult [AGENTS.md](AGENTS.md) for design guidelines, grid rules, and compilation instructions.

---

## 🚀 How to View & Edit

### Option 1: PowerPoint Poster (`pptx/`) — *Penn State CoE & MPC Print Compliant*
- **Edit Directly:** Open [`pptx/Kolsky_Poster.pptx`](pptx/Kolsky_Poster.pptx) in Microsoft PowerPoint. All text boxes, cards, labels, and tables are fully editable native vector shapes.
- **Printing Compliance:** Formatted to **24" $\times$ 32"** portrait, exactly matching the Penn State Multimedia & Print Center (MPC) 24" paper roll width with $\ge 0.5"$ safe mechanical margins.
- **Export to PDF:** Use `File > Save As > PDF` in PowerPoint, or run the automated COM export script:
  ```powershell
  powershell -ExecutionPolicy Bypass -File scripts\export_pptx_to_pdf.ps1
  ```
- **Regenerate from Source:**
  ```powershell
  python scripts/generate_pptx_poster.py
  ```

### Option 2: HTML/CSS Poster (`html/`) — *Fastest Web & Headless Iteration*
- **View / Edit:** Double-click [`html/poster.html`](html/poster.html) to open in any web browser (Chrome or Edge). Edit the text or styling directly in any editor.
- **Export to PDF:** Press `Ctrl + P` in Chrome/Edge, select **Save as PDF**, and ensure paper size is set to **24" $\times$ 32"** (with background graphics enabled).
- **Headless Build:**
  ```powershell
  Start-Process -FilePath "chrome.exe" -ArgumentList '--headless=new', '--no-pdf-header-footer', '--run-all-compositor-stages-before-draw', '--print-to-pdf="html\Kolsky_Poster_HTML.pdf"', 'file:///' + (Resolve-Path "html\poster.html") -Wait -NoNewWindow
  ```

### Option 3: LaTeX Poster (`latex/`)
- Navigate to the `latex/` directory and compile with `pdflatex`:
  ```powershell
  cd latex
  pdflatex -jobname=Kolsky_Poster_LaTeX -interaction=nonstopmode main.tex
  ```
- Compiled PDF: [`latex/Kolsky_Poster_LaTeX.pdf`](latex/Kolsky_Poster_LaTeX.pdf)
