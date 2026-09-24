"""
Generate a professional, publication-quality 24" x 32" PowerPoint research poster
adhering to Penn State College of Engineering & Multimedia/Print Center (MPC) guidelines.

Institutions: The Pennsylvania State University & Los Alamos National Laboratory
Dimensions: 24 in x 32 in (Portrait) - standard 24" roll width
Color Palette: Penn State Navy (#0B2545), Mid-Blue (#1F4E8C), Gold (#D49B28), Ice Tint (#F0F5FA)
"""

import os
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_poster():
    # 1. Initialize presentation & set 24" x 32" dimensions
    prs = Presentation()
    prs.slide_width = Inches(24)
    prs.slide_height = Inches(32)
    blank_layout = prs.slide_layouts[6] # blank layout
    slide = prs.slides.add_slide(blank_layout)

    # Base path resolution
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    img_dir = os.path.join(base_dir, "images")

    # Brand Colors
    NAVY = RGBColor(11, 37, 69)        # #0B2545
    NAVY_DARK = RGBColor(7, 25, 48)    # #071930
    MID_BLUE = RGBColor(31, 78, 140)   # #1F4E8C
    GOLD = RGBColor(212, 155, 40)      # #D49B28
    GOLD_LIGHT = RGBColor(255, 249, 230)
    ICE_BLUE = RGBColor(240, 245, 250) # #F0F5FA
    BG_CANVAS = RGBColor(248, 250, 252)# #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)
    BORDER_GRAY = RGBColor(203, 213, 225) # #CBD5E1
    WHITE = RGBColor(255, 255, 255)
    TEXT_DARK = RGBColor(15, 23, 42)   # #0F172A
    TEXT_MUTED = RGBColor(71, 85, 105) # #475569

    # Canvas Background
    canvas_bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(24), Inches(32)
    )
    canvas_bg.fill.solid()
    canvas_bg.fill.fore_color.rgb = BG_CANVAS
    canvas_bg.line.fill.background() # no border

    # =========================================================
    # 1. TOP HEADER BANNER (Full 24" Width with Safe Inset)
    # =========================================================
    hdr_left = Inches(0.55)
    hdr_top = Inches(0.35)
    hdr_w = Inches(22.90)
    hdr_h = Inches(3.30)

    hdr_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, hdr_left, hdr_top, hdr_w, hdr_h
    )
    hdr_box.fill.solid()
    hdr_box.fill.fore_color.rgb = WHITE
    hdr_box.line.color.rgb = BORDER_GRAY
    hdr_box.line.width = Pt(1.5)

    # Top accent stripes
    stripe1 = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, hdr_left, hdr_top, hdr_w, Inches(0.08)
    )
    stripe1.fill.solid()
    stripe1.fill.fore_color.rgb = NAVY
    stripe1.line.fill.background()

    stripe2 = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, hdr_left, hdr_top + Inches(0.08), hdr_w, Inches(0.04)
    )
    stripe2.fill.solid()
    stripe2.fill.fore_color.rgb = GOLD
    stripe2.line.fill.background()

    # Bottom accent stripes
    stripe3 = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, hdr_left, hdr_top + hdr_h - Inches(0.12), hdr_w, Inches(0.04)
    )
    stripe3.fill.solid()
    stripe3.fill.fore_color.rgb = GOLD
    stripe3.line.fill.background()

    stripe4 = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, hdr_left, hdr_top + hdr_h - Inches(0.08), hdr_w, Inches(0.08)
    )
    stripe4.fill.solid()
    stripe4.fill.fore_color.rgb = NAVY
    stripe4.line.fill.background()

    # Penn State Logo (Left)
    psu_logo_path = os.path.join(img_dir, "PSULogo_hires.png")
    psu_w = Inches(4.18)
    psu_h = Inches(1.30)
    if os.path.exists(psu_logo_path):
        slide.shapes.add_picture(
            psu_logo_path, hdr_left + Inches(0.40), hdr_top + Inches(1.00),
            width=psu_w, height=psu_h
        )

    # LANL Logo (Right) - calculate exact position and aspect ratio
    lanl_logo_path = os.path.join(img_dir, "LANLLogo.png")
    lanl_h = Inches(1.15)
    lanl_w = Inches(1.15 * 3.938) # ~4.53 in
    if os.path.exists(lanl_logo_path):
        slide.shapes.add_picture(
            lanl_logo_path, hdr_left + hdr_w - lanl_w - Inches(0.45), hdr_top + Inches(1.05),
            width=lanl_w, height=lanl_h
        )

    # Center Text Block (Title, Subtitle, Authors, Affiliation)
    title_left = hdr_left + psu_w + Inches(0.65)
    title_w = hdr_w - (psu_w + lanl_w + Inches(1.50))
    title_box = slide.shapes.add_textbox(title_left, hdr_top + Inches(0.32), title_w, Inches(2.70))
    tf = title_box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0)
    tf.margin_right = Inches(0)
    tf.margin_top = Inches(0)
    tf.margin_bottom = Inches(0)

    # Title
    p_title = tf.paragraphs[0]
    p_title.alignment = PP_ALIGN.CENTER
    p_title.space_after = Pt(4)
    run_title = p_title.add_run()
    run_title.text = "High-Throughput Dynamic Material Characterization"
    run_title.font.name = "Arial"
    run_title.font.size = Pt(27)
    run_title.font.bold = True
    run_title.font.color.rgb = NAVY

    # Subtitle
    p_sub = tf.add_paragraph()
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.space_after = Pt(9)
    run_sub = p_sub.add_run()
    run_sub.text = "Synergistic Experimental & Digital Twin Framework for Rate-Dependent Model Discovery"
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(15.5)
    run_sub.font.bold = True
    run_sub.font.color.rgb = MID_BLUE

    # Authors
    p_auth = tf.add_paragraph()
    p_auth.alignment = PP_ALIGN.CENTER
    p_auth.space_after = Pt(3)
    
    r_a1 = p_auth.add_run()
    r_a1.text = "Zachary Salas¹    "
    r_a1.font.name = "Arial"
    r_a1.font.size = Pt(13)
    r_a1.font.bold = True
    r_a1.font.color.rgb = NAVY

    r_sep1 = p_auth.add_run()
    r_sep1.text = "|    "
    r_sep1.font.name = "Arial"
    r_sep1.font.size = Pt(13)
    r_sep1.font.color.rgb = GOLD

    r_a2 = p_auth.add_run()
    r_a2.text = "Jeremy Croom¹    "
    r_a2.font.name = "Arial"
    r_a2.font.size = Pt(13)
    r_a2.font.bold = True
    r_a2.font.color.rgb = NAVY

    r_sep2 = p_auth.add_run()
    r_sep2.text = "|    "
    r_sep2.font.name = "Arial"
    r_sep2.font.size = Pt(13)
    r_sep2.font.color.rgb = GOLD

    r_a3 = p_auth.add_run()
    r_a3.text = "Reuben H. Kraft, Ph.D.¹"
    r_a3.font.name = "Arial"
    r_a3.font.size = Pt(13)
    r_a3.font.bold = True
    r_a3.font.color.rgb = NAVY

    # Affiliation
    p_aff = tf.add_paragraph()
    p_aff.alignment = PP_ALIGN.CENTER
    run_aff = p_aff.add_run()
    run_aff.text = "¹Department of Mechanical Engineering, The Pennsylvania State University, University Park, PA"
    run_aff.font.name = "Arial"
    run_aff.font.size = Pt(10.5)
    run_aff.font.color.rgb = TEXT_MUTED

    # =========================================================
    # REUSABLE CARD BUILDER FUNCTION
    # =========================================================
    col1_left = Inches(0.55)
    col_w = Inches(11.25)
    col_gap = Inches(0.40)
    col2_left = col1_left + col_w + col_gap # 12.20 in

    def create_card_shell(left, top, width, height, title, badge_text, badge_gold=False):
        # Outer Card Container
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
        )
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_GRAY
        card.line.width = Pt(1.2)

        # Header Banner
        hdr_bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, left, top, width, Inches(0.60)
        )
        hdr_bar.fill.solid()
        hdr_bar.fill.fore_color.rgb = NAVY
        hdr_bar.line.fill.background()

        # Gold Header Accent Stripe
        hdr_gold = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, left, top + Inches(0.60), width, Inches(0.04)
        )
        hdr_gold.fill.solid()
        hdr_gold.fill.fore_color.rgb = GOLD
        hdr_gold.line.fill.background()

        # Header Title Text
        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.05), width - Inches(2.80), Inches(0.50))
        p = tb.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        tb.text_frame.margin_left = Inches(0)
        tb.text_frame.margin_top = Inches(0.05)
        run = p.add_run()
        run.text = title
        run.font.name = "Arial"
        run.font.size = Pt(13.5)
        run.font.bold = True
        run.font.color.rgb = WHITE

        # Category Badge (Top Right)
        badge_w = Inches(2.20)
        badge_h = Inches(0.38)
        badge_left = left + width - badge_w - Inches(0.20)
        badge_top = top + Inches(0.11)

        badge = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, badge_left, badge_top, badge_w, badge_h
        )
        badge.fill.solid()
        badge.fill.fore_color.rgb = GOLD if badge_gold else MID_BLUE
        badge.line.fill.background()

        btb = slide.shapes.add_textbox(badge_left, badge_top, badge_w, badge_h)
        bp = btb.text_frame.paragraphs[0]
        bp.alignment = PP_ALIGN.CENTER
        btb.text_frame.margin_top = Inches(0.05)
        brun = bp.add_run()
        brun.text = badge_text.upper()
        brun.font.name = "Arial"
        brun.font.size = Pt(8.5)
        brun.font.bold = True
        brun.font.color.rgb = NAVY if badge_gold else WHITE

    def add_bullets(left, top, width, height, items, font_size=10.2, space_after=5):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.05)
        tf.margin_right = Inches(0.05)
        tf.margin_top = Inches(0.05)
        tf.margin_bottom = Inches(0.05)

        for i, (title_text, body_text) in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(space_after)
            p.alignment = PP_ALIGN.LEFT

            # Custom Bullet Symbol (Gold square)
            r_bullet = p.add_run()
            r_bullet.text = "▪ "
            r_bullet.font.name = "Arial"
            r_bullet.font.size = Pt(font_size + 2)
            r_bullet.font.bold = True
            r_bullet.font.color.rgb = GOLD

            # Bold Title
            r_bold = p.add_run()
            r_bold.text = title_text + ": "
            r_bold.font.name = "Arial"
            r_bold.font.size = Pt(font_size)
            r_bold.font.bold = True
            r_bold.font.color.rgb = NAVY

            # Normal Text
            r_body = p.add_run()
            r_body.text = body_text
            r_body.font.name = "Arial"
            r_body.font.size = Pt(font_size)
            r_body.font.color.rgb = TEXT_DARK

    # =========================================================
    # ROW 1: MINIATURE KOLSKY BAR & DIGITAL TWIN
    # =========================================================
    row1_top = Inches(3.85)
    row1_h = Inches(8.15)

    # --- CARD 1: Miniature Kolsky Bar Apparatus ---
    create_card_shell(col1_left, row1_top, col_w, row1_h,
                      "Miniature Kolsky Bar Apparatus (Ø 3.17 mm)",
                      "Experimental Apparatus")

    # Card 1 Hardware Photo
    c1_img_path = os.path.join(img_dir, "PSU_MiniKolskyBar_system.png")
    if os.path.exists(c1_img_path):
        slide.shapes.add_picture(
            c1_img_path, col1_left + Inches(0.22), row1_top + Inches(0.75),
            width=Inches(5.75), height=Inches(3.40)
        )

    # Card 1 Hardware Architecture Table Box
    spec_left = col1_left + Inches(6.12)
    spec_top = row1_top + Inches(0.75)
    spec_w = Inches(4.90)
    spec_h = Inches(3.40)

    spec_bg = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, spec_left, spec_top, spec_w, spec_h
    )
    spec_bg.fill.solid()
    spec_bg.fill.fore_color.rgb = ICE_BLUE
    spec_bg.line.color.rgb = BORDER_GRAY
    spec_bg.line.width = Pt(1.0)

    # Spec header strip
    spec_hdr = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, spec_left, spec_top, spec_w, Inches(0.38)
    )
    spec_hdr.fill.solid()
    spec_hdr.fill.fore_color.rgb = MID_BLUE
    spec_hdr.line.fill.background()

    spec_tb = slide.shapes.add_textbox(spec_left, spec_top + Inches(0.04), spec_w, Inches(0.32))
    sp_p = spec_tb.text_frame.paragraphs[0]
    sp_p.alignment = PP_ALIGN.CENTER
    s_run = sp_p.add_run()
    s_run.text = "HARDWARE ARCHITECTURE"
    s_run.font.name = "Arial"
    s_run.font.size = Pt(8.8)
    s_run.font.bold = True
    s_run.font.color.rgb = WHITE

    # Spec content rows
    specs_data = [
        ("Bar Material:", "C350 Maraging Steel"),
        ("Bar Diameter:", "Ø 3.17 mm (1/8″ OD)"),
        ("Bar Lengths:", "Inc. 1.0 m, Trans. 1.0 m"),
        ("Wave Speed:", "C₀ ≈ 4,960 m/s"),
        ("Striker Range:", "Lₛ = 200 mm, V₀ ≤ 30 m/s"),
        ("Pulse Duration:", "Tₚ ≈ 78 μs"),
        ("Diagnostics:", "Semiconductor (10 MHz DAQ)"),
        ("Strain Rate:", "ε̇_max ~ 1.2 × 10⁴ s⁻¹")
    ]

    spec_list_tb = slide.shapes.add_textbox(spec_left + Inches(0.14), spec_top + Inches(0.44), spec_w - Inches(0.28), Inches(2.85))
    s_tf = spec_list_tb.text_frame
    s_tf.margin_top = Inches(0.02)
    s_tf.margin_bottom = Inches(0.02)

    for i, (lbl, val) in enumerate(specs_data):
        p = s_tf.paragraphs[0] if i == 0 else s_tf.add_paragraph()
        p.space_after = Pt(3.2)
        r_l = p.add_run()
        r_l.text = f"{lbl:<15} "
        r_l.font.name = "Arial"
        r_l.font.size = Pt(8.8)
        r_l.font.bold = True
        r_l.font.color.rgb = NAVY

        r_v = p.add_run()
        r_v.text = val
        r_v.font.name = "Arial"
        r_v.font.size = Pt(8.8)
        r_v.font.color.rgb = TEXT_DARK

    # Card 1 Bullets (generous font size to fill card evenly)
    c1_bullets = [
        ("Ultra-Small Diameter Architecture", "Precision Ø 3.17 mm C350 maraging steel bar system specifically engineered for sub-scale testing of advanced composites, ductile metals (OFHC copper), and transparent polymers (PMMA)."),
        ("Extreme Dynamic Strain Rate Regime", "Achieves dynamic strain rates from ε̇ ~ 10³ to 1.2 × 10⁴ s⁻¹ under strictly verified 1D wave propagation with minimal Pochhammer-Chree radial dispersion."),
        ("High-Frequency Diagnostics", "Instrumented with high-bandwidth semiconductor strain gauges at bar midpoints; isolates incident (σᵢ), reflected (σᵣ), and transmitted (σₜ) stress waves digitized at 10 MHz."),
        ("High-Throughput Testing Protocol", "Modular alignment guides and precision collets enable rapid shot cycles (>10 shots/hr), providing dense empirical datasets for statistical uncertainty bounds.")
    ]
    add_bullets(col1_left + Inches(0.22), row1_top + Inches(4.30), col_w - Inches(0.44), Inches(3.70), c1_bullets, font_size=10.4, space_after=6.0)

    # --- CARD 2: Abaqus/Explicit Digital Twin Modeling ---
    create_card_shell(col2_left, row1_top, col_w, row1_h,
                      "Abaqus/Explicit Digital Twin Modeling",
                      "Computational Twin")

    # Digital Twin Schematic & Mesh Zoom Image
    c2_img_path = os.path.join(img_dir, "digital_twin_full_and_zoom.png")
    if os.path.exists(c2_img_path):
        slide.shapes.add_picture(
            c2_img_path, col2_left + Inches(0.22), row1_top + Inches(0.75),
            width=col_w - Inches(0.44), height=Inches(2.35)
        )

    # Card 2 Upper Bullets
    c2_top_bullets = [
        ("Multi-Symmetry FE Formulations", "3D quarter- and full-symmetry models constructed in Abaqus/Explicit with C3D8R hex elements for dispersive wave propagation, striker impact, and boundary condition verification."),
        ("Pre-Shot Waveform Optimization", "Virtual striker velocity and boundary impedance sweeps eliminate trial-and-error testing and maximize constant-strain-rate deformation duration.")
    ]
    add_bullets(col2_left + Inches(0.22), row1_top + Inches(3.18), col_w - Inches(0.44), Inches(1.35), c2_top_bullets, font_size=9.8, space_after=4.0)

    # Sub-panel: Innovative Pulse Shaping for Tailored Response
    sub_left = col2_left + Inches(0.22)
    sub_top = row1_top + Inches(4.65)
    sub_w = col_w - Inches(0.44)
    sub_h = Inches(3.35)

    sub_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, sub_left, sub_top, sub_w, sub_h
    )
    sub_box.fill.solid()
    sub_box.fill.fore_color.rgb = ICE_BLUE
    sub_box.line.color.rgb = BORDER_GRAY
    sub_box.line.width = Pt(1.0)

    # Sub-header strip
    sub_hdr = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, sub_left, sub_top, sub_w, Inches(0.36)
    )
    sub_hdr.fill.solid()
    sub_hdr.fill.fore_color.rgb = MID_BLUE
    sub_hdr.line.fill.background()

    sub_title_tb = slide.shapes.add_textbox(sub_left + Inches(0.15), sub_top + Inches(0.04), sub_w - Inches(2.20), Inches(0.30))
    st_p = sub_title_tb.text_frame.paragraphs[0]
    st_run = st_p.add_run()
    st_run.text = "INNOVATIVE PULSE SHAPING FOR TAILORED RESPONSE"
    st_run.font.name = "Arial"
    st_run.font.size = Pt(8.8)
    st_run.font.bold = True
    st_run.font.color.rgb = WHITE

    # Sub badge
    sub_badge = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, sub_left + sub_w - Inches(2.05), sub_top + Inches(0.05), Inches(1.95), Inches(0.26)
    )
    sub_badge.fill.solid()
    sub_badge.fill.fore_color.rgb = GOLD
    sub_badge.line.fill.background()

    sb_tb = slide.shapes.add_textbox(sub_left + sub_w - Inches(2.05), sub_top + Inches(0.04), Inches(1.95), Inches(0.26))
    sb_p = sb_tb.text_frame.paragraphs[0]
    sb_p.alignment = PP_ALIGN.CENTER
    sb_run = sb_p.add_run()
    sb_run.text = "TAILORED WAVEFORMS"
    sb_run.font.name = "Arial"
    sb_run.font.size = Pt(7.8)
    sb_run.font.bold = True
    sb_run.font.color.rgb = NAVY

    # Sub image & bullets side-by-side
    pulse_img_path = os.path.join(img_dir, "pulse_shaping_tailored_response.png")
    if os.path.exists(pulse_img_path):
        slide.shapes.add_picture(
            pulse_img_path, sub_left + Inches(0.15), sub_top + Inches(0.46),
            width=Inches(4.90), height=Inches(2.75)
        )

    sub_bullets = [
        ("AM Micro-Architected Shapers", "Additively manufactured micro-lattices (nTopology/Abaqus) engineered to eliminate high-frequency wave dispersion and initial stress spikes."),
        ("Constant Strain-Rate Control", "Programmable rise times dynamically tailor the incident pulse to ensure dynamic equilibrium and steady ε̇ deformation across soft and hard materials.")
    ]
    add_bullets(sub_left + Inches(5.15), sub_top + Inches(0.50), sub_w - Inches(5.25), Inches(2.75), sub_bullets, font_size=9.5, space_after=5.0)

    # =========================================================
    # WORKFLOW RIBBON: 4-Step Closed-Loop Pipeline
    # =========================================================
    wf_left = Inches(0.55)
    wf_top = Inches(12.18)
    wf_w = Inches(22.90)
    wf_h = Inches(1.30)

    wf_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, wf_left, wf_top, wf_w, wf_h
    )
    wf_box.fill.solid()
    wf_box.fill.fore_color.rgb = WHITE
    wf_box.line.color.rgb = BORDER_GRAY
    wf_box.line.width = Pt(1.2)

    # Left accent label
    wf_tag = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, wf_left, wf_top, Inches(0.12), wf_h
    )
    wf_tag.fill.solid()
    wf_tag.fill.fore_color.rgb = GOLD
    wf_tag.line.fill.background()

    # 4 Steps
    steps_data = [
        ("1. Virtual Pulse Shaping", "Abaqus sweeps shaper geometry & velocity", NAVY),
        ("2. Specimen & Shaper Prep", "Wire-EDM precision fabrication & alignment", MID_BLUE),
        ("3. Dynamic Mini-SHPB Run", "10 MHz strain acquisition + Nova S20 video", NAVY),
        ("4. Model Calibration & Discovery", "Extract σ-ε curves & refine digital twin", MID_BLUE)
    ]

    card_step_w = Inches(5.05)
    card_step_h = Inches(1.00)
    card_step_y = wf_top + Inches(0.15)
    arrow_w = Inches(0.50)

    cur_x = wf_left + Inches(0.35)
    for i, (stitle, sdesc, scolor) in enumerate(steps_data):
        # Step Card
        sc = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, cur_x, card_step_y, card_step_w, card_step_h
        )
        sc.fill.solid()
        sc.fill.fore_color.rgb = scolor
        sc.line.fill.background()

        # Step Text
        stb = slide.shapes.add_textbox(cur_x + Inches(0.15), card_step_y + Inches(0.10), card_step_w - Inches(0.30), card_step_h - Inches(0.20))
        stf = stb.text_frame
        stf.word_wrap = True
        stf.margin_top = Inches(0)
        stf.margin_bottom = Inches(0)

        p1 = stf.paragraphs[0]
        p1.alignment = PP_ALIGN.CENTER
        p1.space_after = Pt(2)
        r1 = p1.add_run()
        r1.text = stitle
        r1.font.name = "Arial"
        r1.font.size = Pt(11.0)
        r1.font.bold = True
        r1.font.color.rgb = WHITE

        p2 = stf.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        r2 = p2.add_run()
        r2.text = sdesc
        r2.font.name = "Arial"
        r2.font.size = Pt(9.0)
        r2.font.color.rgb = GOLD_LIGHT if scolor == NAVY else ICE_BLUE

        cur_x += card_step_w

        # Connecting Arrow
        if i < len(steps_data) - 1:
            arr_tb = slide.shapes.add_textbox(cur_x, card_step_y + Inches(0.25), arrow_w, Inches(0.50))
            ap = arr_tb.text_frame.paragraphs[0]
            ap.alignment = PP_ALIGN.CENTER
            arun = ap.add_run()
            arun.text = "▶"
            arun.font.name = "Arial"
            arun.font.size = Pt(16)
            arun.font.bold = True
            arun.font.color.rgb = GOLD
            cur_x += arrow_w

    # =========================================================
    # ROW 2: WAVE ALIGNMENT & HIGH-SPEED VIDEO
    # =========================================================
    row2_top = Inches(13.65)
    row2_h = Inches(8.40)

    # --- CARD 3: Dynamic Wave Alignment & Validation ---
    create_card_shell(col1_left, row2_top, col_w, row2_h,
                      "Dynamic Wave Alignment & Validation",
                      "Wave Propagation")

    # Stacked Waveform Images side-by-side
    inc_img_path = os.path.join(img_dir, "incidentcomp.png")
    trans_img_path = os.path.join(img_dir, "transmissioncomp.png")
    if os.path.exists(inc_img_path) and os.path.exists(trans_img_path):
        slide.shapes.add_picture(
            inc_img_path, col1_left + Inches(0.22), row2_top + Inches(0.75),
            width=Inches(5.35), height=Inches(3.30)
        )
        slide.shapes.add_picture(
            trans_img_path, col1_left + Inches(5.68), row2_top + Inches(0.75),
            width=Inches(5.35), height=Inches(3.30)
        )

    # Card 3 Bullets
    c3_bullets = [
        ("Dispersion-Corrected Voltage Signals", "Incident and transmitted pulses captured at 10 MHz sampling frequency; wave profiles time-shifted to specimen contact interface."),
        ("Digital Twin Predictive Accuracy", "Tight overlay between finite element simulation predictions and experimental bridge voltages across the primary pulse duration."),
        ("Dynamic Force Equilibrium", "Verified across incident and transmission bar platens (P₁(t) ≈ P₂(t)), ensuring homogeneous stress distribution throughout deformation."),
        ("Model Refinement Feedback", "Waveform discrepancies directly guide the identification of rate-dependent strain hardening and thermal softening parameters.")
    ]
    add_bullets(col1_left + Inches(0.22), row2_top + Inches(4.20), col_w - Inches(0.44), Inches(4.00), c3_bullets, font_size=10.2, space_after=5.5)

    # --- CARD 4: Photron FASTCAM Nova S20 High-Speed Video ---
    create_card_shell(col2_left, row2_top, col_w, row2_h,
                      "Photron FASTCAM Nova S20 High-Speed Video",
                      "Optical Diagnostics")

    # Top camera row: Photo + Sync Text
    cam_img_path = os.path.join(img_dir, "camera_setup.jpg")
    if os.path.exists(cam_img_path):
        slide.shapes.add_picture(
            cam_img_path, col2_left + Inches(0.22), row2_top + Inches(0.75),
            width=Inches(3.60), height=Inches(2.15)
        )

    # Camera Sync Details Box
    cam_tb = slide.shapes.add_textbox(col2_left + Inches(3.95), row2_top + Inches(0.70), col_w - Inches(4.17), Inches(2.20))
    ctf = cam_tb.text_frame
    ctf.word_wrap = True
    ctf.margin_top = Inches(0)
    ctf.margin_left = Inches(0.05)

    cp1 = ctf.paragraphs[0]
    cp1.space_after = Pt(2)
    c_r1 = cp1.add_run()
    c_r1.text = "Optical Configuration & Sync:"
    c_r1.font.name = "Arial"
    c_r1.font.size = Pt(11.0)
    c_r1.font.bold = True
    c_r1.font.color.rgb = NAVY

    cp2 = ctf.add_paragraph()
    cp2.space_after = Pt(4)
    c_r2 = cp2.add_run()
    c_r2.text = "Coupled with macro-telephoto optics and high-intensity LED matrix illumination, triggered synchronously with the incident strain bridge."
    c_r2.font.name = "Arial"
    c_r2.font.size = Pt(9.5)
    c_r2.font.color.rgb = TEXT_DARK

    cam_sub_bullets = [
        ("Framing Rates", "100,000 to 200,000 fps with sub-μs exposure to freeze dynamic wave motion."),
        ("Alignment Verification", "Real-time visualization guarantees coaxial platen impact without bar bending.")
    ]
    for btitle, bbody in cam_sub_bullets:
        p = ctf.add_paragraph()
        p.space_after = Pt(2.5)
        r_b = p.add_run()
        r_b.text = "▪ "
        r_b.font.size = Pt(10)
        r_b.font.bold = True
        r_b.font.color.rgb = GOLD
        r_t = p.add_run()
        r_t.text = btitle + ": "
        r_t.font.size = Pt(9.4)
        r_t.font.bold = True
        r_t.font.color.rgb = NAVY
        r_d = p.add_run()
        r_d.text = bbody
        r_d.font.size = Pt(9.4)
        r_d.font.color.rgb = TEXT_DARK

    # Filmstrip Sequence Container
    film_left = col2_left + Inches(0.22)
    film_top = row2_top + Inches(3.00)
    film_w = col_w - Inches(0.44)
    film_h = Inches(2.45)

    film_bg = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, film_left, film_top, film_w, film_h
    )
    film_bg.fill.solid()
    film_bg.fill.fore_color.rgb = ICE_BLUE
    film_bg.line.color.rgb = BORDER_GRAY
    film_bg.line.width = Pt(1.0)

    # Filmstrip Title
    ft_tb = slide.shapes.add_textbox(film_left, film_top + Inches(0.04), film_w, Inches(0.30))
    ftp = ft_tb.text_frame.paragraphs[0]
    ftp.alignment = PP_ALIGN.CENTER
    ft_run = ftp.add_run()
    ft_run.text = "High-Speed Dynamic Compression Sequence (ε̇ ~ 4000 s⁻¹ OFHC Copper on Ø 3.17 mm Bars)"
    ft_run.font.name = "Arial"
    ft_run.font.size = Pt(8.8)
    ft_run.font.bold = True
    ft_run.font.color.rgb = MID_BLUE

    # 5 High-Speed Frames
    frame_w = Inches(2.00)
    frame_h = Inches(1.50)
    frame_y = film_top + Inches(0.38)
    frame_gap = (film_w - (frame_w * 5)) / 6

    frames_meta = [
        ("copper_f1.png", "0.0 μs", "Initial"),
        ("copper_f2.png", "35.0 μs", "Elastic"),
        ("copper_f3.png", "70.0 μs", "Flow"),
        ("copper_f4.png", "105.0 μs", "Barreling"),
        ("copper_f5.png", "140.0 μs", "Perm. Set")
    ]

    for idx, (fimg, ftime, fstate) in enumerate(frames_meta):
        fx = film_left + frame_gap + idx * (frame_w + frame_gap)
        fpath = os.path.join(img_dir, fimg)
        if os.path.exists(fpath):
            slide.shapes.add_picture(fpath, fx, frame_y, width=frame_w, height=frame_h)

        # Tag bar below image
        tag_tb = slide.shapes.add_textbox(fx, frame_y + frame_h + Inches(0.02), frame_w, Inches(0.35))
        tag_tf = tag_tb.text_frame
        tag_tf.margin_top = Inches(0)
        tp = tag_tf.paragraphs[0]
        tp.alignment = PP_ALIGN.CENTER
        tr1 = tp.add_run()
        tr1.text = f"{ftime}  "
        tr1.font.name = "Arial"
        tr1.font.size = Pt(7.8)
        tr1.font.bold = True
        tr1.font.color.rgb = GOLD

        tr2 = tp.add_run()
        tr2.text = f"[{fstate}]"
        tr2.font.name = "Arial"
        tr2.font.size = Pt(7.8)
        tr2.font.bold = True
        tr2.font.color.rgb = NAVY

    # Card 4 Lower Bullets
    c4_bullets = [
        ("Deformation Kinematics", "In-situ high-speed sequence captures progressive axial upsetting, uniform radial expansion, and plastic barreling without shear localization."),
        ("Dynamic Contact Uniformity", "Sub-microsecond exposure verifies planar platen seating and absence of specimen tilt or reverberating acoustic reflections during wave entry."),
        ("Full-Field Optical Strain Tracking", "Synchronous frame recordings enable DIC to cross-validate bar 1D wave reduction against true surface kinematics.")
    ]
    add_bullets(col2_left + Inches(0.22), row2_top + Inches(5.55), col_w - Inches(0.44), Inches(2.70), c4_bullets, font_size=9.8, space_after=4.0)

    # =========================================================
    # ROW 3: RATE DEPENDENCE & AUTONOMOUS FACILITY
    # =========================================================
    row3_top = Inches(22.25)
    row3_h = Inches(9.20)

    # --- CARD 5: Rate-Dependent Response & Failure Diagnostics ---
    create_card_shell(col1_left, row3_top, col_w, row3_h,
                      "Rate-Dependent Response & Failure Diagnostics",
                      "Material Behavior")

    # Rate and Damage Composite Plot & SEM Micrographs
    c5_img_path = os.path.join(img_dir, "rate_and_damage_composite.png")
    if os.path.exists(c5_img_path):
        slide.shapes.add_picture(
            c5_img_path, col1_left + Inches(0.22), row3_top + Inches(0.75),
            width=col_w - Inches(0.44), height=Inches(3.95)
        )

    # Card 5 Bullets
    c5_bullets = [
        ("Extended Constant Strain-Rate Plateau", "Tailored pulse shaping yields a flat strain-rate plateau (ε̇ ≈ 3,400–3,560 s⁻¹), ensuring constitutive data is uncontaminated by transient wave accelerations."),
        ("Dynamic Yield & Flow Enhancement", "PMMA specimens exhibit distinct rate hardening, elevating flow stress to ~345 MPa at high rates compared to quasi-static yield values (~100 MPa)."),
        ("Micro-Scale Failure Mechanisms", "Post-test SEM imaging reveals transverse fiber shear kinking, matrix crushing, and dynamic spallation at rates >10³ s⁻¹."),
        ("Symbiotic Digital Twin Feedback", "Experimental flow stress curves and 3D micro-CT damage fields directly inform and calibrate anisotropic plasticity and dynamic failure criteria in LANL penetration simulations.")
    ]
    add_bullets(col1_left + Inches(0.22), row3_top + Inches(4.85), col_w - Inches(0.44), Inches(4.20), c5_bullets, font_size=10.2, space_after=5.5)

    # --- CARD 6: Future Horizons: Autonomous Kolsky Bar System ---
    create_card_shell(col2_left, row3_top, col_w, row3_h,
                      "Future Horizons: Autonomous Kolsky Bar System",
                      "1,000 Tests / Day", badge_gold=True)

    # Automation Architecture Concept Diagram (Cleaned feedback loop!)
    c6_img_path = os.path.join(img_dir, "automation_concept.png")
    if os.path.exists(c6_img_path):
        slide.shapes.add_picture(
            c6_img_path, col2_left + Inches(0.22), row3_top + Inches(0.75),
            width=col_w - Inches(0.44), height=Inches(3.95)
        )

    # Card 6 Bullets
    c6_bullets = [
        ("Autonomous 1,000-Tests/Day Throughput", "High-density robotic carousels, automated pick-and-place micro-grippers (±5 μm), and rapid-cycle pulse-shaper cassettes achieve <60 s shot turnaround."),
        ("Multi-Condition Parametric Testing", "Rapid automated sweeps across wide thermal bounds (−150°C to 800°C), strain rates (10²–10⁴ s⁻¹), and multi-axial stress states (compression, shear, tension)."),
        ("Active Learning Experiment Steering", "Bayesian acquisition algorithms identify high-uncertainty regions in constitutive space, automatically commanding the next test conditions to maximize information gain."),
        ("Automated Rate-Dependent Model Discovery", "Synchronized 10 MHz DAQ and DIC feed into automated inverse FE solvers, auto-calibrating Johnson-Cook and damage models for direct LANL hydrocode deployment.")
    ]
    add_bullets(col2_left + Inches(0.22), row3_top + Inches(4.85), col_w - Inches(0.44), Inches(4.20), c6_bullets, font_size=10.2, space_after=5.5)

    # Output PPTX
    out_dir = os.path.join(base_dir, "pptx")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Kolsky_Poster.pptx")
    prs.save(out_path)
    print(f"Successfully generated PowerPoint poster at: {out_path}")

if __name__ == "__main__":
    create_poster()
