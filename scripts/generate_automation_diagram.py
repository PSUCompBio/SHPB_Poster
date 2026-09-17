import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle
import numpy as np

# Set up figure with high DPI and professional aesthetic
fig, ax = plt.subplots(figsize=(16, 5.5), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

# Set canvas limits
ax.set_xlim(0, 16)
ax.set_ylim(0, 5.5)
ax.axis('off')

# Color palette (Penn State Navy, Gold, Clean Slate Blues)
c_navy = '#0B2545'
c_navy_light = '#13315C'
c_blue = '#1F4E8C'
c_ice = '#F0F5FA'
c_gold = '#D49B28'
c_gold_light = '#FFF9E6'
c_border = '#BACEE0'
c_text_dark = '#0B2545'
c_text_muted = '#4A5568'
c_green = '#1B7A42'

# Top Header Bar
header_bg = FancyBboxPatch((0.3, 4.6), 15.4, 0.75,
                           boxstyle="round,pad=0.08,rounding_size=0.15",
                           facecolor=c_navy, edgecolor=c_gold, linewidth=1.5)
ax.add_patch(header_bg)

ax.text(0.6, 4.98, "AUTONOMOUS HIGH-THROUGHPUT KOLSKY BAR ARCHITECTURE",
        fontsize=13.5, fontweight='bold', color='white', va='center')
ax.text(0.6, 4.75, "Closed-Loop Robotic Testing, In-Situ Multi-Modal Diagnostics & Digital Twin Model Generation",
        fontsize=8.5, color='#B0CDE5', va='center')

# Target badge in top right
badge_bg = FancyBboxPatch((12.1, 4.68), 3.5, 0.58,
                          boxstyle="round,pad=0.06,rounding_size=0.12",
                          facecolor=c_gold, edgecolor='white', linewidth=1.2)
ax.add_patch(badge_bg)
ax.text(13.85, 4.97, "TARGET: 1,000 TESTS / DAY",
        fontsize=10.5, fontweight='bold', color=c_navy, ha='center', va='center')

# Define 5 Core Workflow Pillars
pillars = [
    {
        "x": 0.3, "w": 2.85, "title": "1. Robotic Loading",
        "badge": "SPECIMEN & SHAPER", "badge_col": c_blue,
        "items": [
            "• High-density specimen carousel",
            "• Automated micro-gripper (±5 µm)",
            "• Rapid-feed pulse-shaper cassette",
            "• Thermal chamber: -150°C to 800°C"
        ],
        "highlight": "Cycle time: < 60 s / shot"
    },
    {
        "x": 3.45, "w": 2.85, "title": "2. High-Rate Bar",
        "badge": "MINI-KOLSKY (Ø3.17 mm)", "badge_col": c_navy_light,
        "items": [
            "• Automated pneumatic launcher",
            "• Striker velocity: 5 to 30 m/s",
            "• Multi-axial: Comp / Tens / Shear",
            "• Laser photogate sync trigger"
        ],
        "highlight": "Rate: 10² to >10⁴ s⁻¹"
    },
    {
        "x": 6.6, "w": 2.85, "title": "3. In-Situ Diagnostics",
        "badge": "10 MHz DAQ & DIC", "badge_col": c_blue,
        "items": [
            "• 10 MHz semiconductor gauges",
            "• Nova S20 video (200,000 fps)",
            "• Real-time DIC displacement fields",
            "• Dynamic platen equilibrium check"
        ],
        "highlight": "Instant P₁(t) ≈ P₂(t) verify"
    },
    {
        "x": 9.75, "w": 2.85, "title": "4. Twin Inversion",
        "badge": "ABAQUS / SURROGATE", "badge_col": c_navy_light,
        "items": [
            "• Automated dispersion correction",
            "• Digital twin inverse parameter fit",
            "• Friction & inertia compensation",
            "• Real-time σ(ε, ε̇, T) extraction"
        ],
        "highlight": "Physics-informed FEA link"
    },
    {
        "x": 12.9, "w": 2.8, "title": "5. Constitutive Library",
        "badge": "AUTO-CALIBRATION", "badge_col": c_green,
        "items": [
            "• Johnson-Cook & Zerilli-Armstrong",
            "• Anisotropic plasticity / damage",
            "• Direct export to LANL hydrocodes",
            "• Statistical variance & bounds"
        ],
        "highlight": "Calibrated material cards"
    }
]

# Draw Cards
for p in pillars:
    x, w = p["x"], p["w"]
    # Outer Card
    card = FancyBboxPatch((x, 1.15), w, 3.25,
                          boxstyle="round,pad=0.06,rounding_size=0.12",
                          facecolor=c_ice, edgecolor=c_border, linewidth=1.2)
    ax.add_patch(card)
    
    # Pillar Header
    hdr = FancyBboxPatch((x, 3.95), w, 0.45,
                         boxstyle="round,pad=0.04,rounding_size=0.08",
                         facecolor=c_navy, edgecolor='none')
    ax.add_patch(hdr)
    ax.text(x + w/2, 4.17, p["title"],
            fontsize=9.5, fontweight='bold', color='white', ha='center', va='center')
    
    # Sub-badge
    badge = FancyBboxPatch((x + 0.15, 3.65), w - 0.3, 0.22,
                           boxstyle="round,pad=0.02,rounding_size=0.05",
                           facecolor=p["badge_col"], edgecolor='none')
    ax.add_patch(badge)
    ax.text(x + w/2, 3.76, p["badge"],
            fontsize=6.8, fontweight='bold', color='white', ha='center', va='center')
    
    # Items
    y_text = 3.35
    for itm in p["items"]:
        ax.text(x + 0.15, y_text, itm, fontsize=7.2, color=c_text_dark, va='center')
        y_text -= 0.38
        
    # Highlight pill at bottom of card
    hl_bg = FancyBboxPatch((x + 0.15, 1.3), w - 0.3, 0.32,
                           boxstyle="round,pad=0.03,rounding_size=0.06",
                           facecolor=c_gold_light, edgecolor=c_gold, linewidth=0.8)
    ax.add_patch(hl_bg)
    ax.text(x + w/2, 1.46, p["highlight"],
            fontsize=7.2, fontweight='bold', color=c_navy, ha='center', va='center')

# Forward Flow Arrows between stages
arrow_positions = [
    (3.15, 2.77),
    (6.3, 2.77),
    (9.45, 2.77),
    (12.6, 2.77)
]

for ax_pos, ay_pos in arrow_positions:
    ax.annotate('', xy=(ax_pos + 0.28, ay_pos), xytext=(ax_pos + 0.02, ay_pos),
                arrowprops=dict(arrowstyle="-|>", color=c_gold, lw=2.5, mutation_scale=14))

# Bottom Loop: Active Learning & Bayesian Experiment Steering Container
loop_bg = FancyBboxPatch((0.3, 0.15), 15.4, 0.72,
                         boxstyle="round,pad=0.05,rounding_size=0.10",
                         facecolor='#EBF3FA', edgecolor=c_blue, linewidth=1.2)
ax.add_patch(loop_bg)

# Left return badge
steer_badge = FancyBboxPatch((0.45, 0.24), 3.45, 0.54,
                             boxstyle="round,pad=0.04,rounding_size=0.08",
                             facecolor=c_blue, edgecolor='none')
ax.add_patch(steer_badge)
ax.text(2.17, 0.51, "BAYESIAN ACTIVE LEARNING", fontsize=8.2, fontweight='bold', color='white', ha='center', va='center')

ax.text(4.15, 0.61, "Autonomous Experiment Steering & Closed-Loop Acquisition Policy:",
        fontsize=8.5, fontweight='bold', color=c_navy, va='center')
ax.text(4.15, 0.36, "Inverse models evaluate constitutive uncertainty to automatically command the robotic carousel and launcher for the next optimal (T, ε̇, stress state) test.",
        fontsize=7.35, color=c_text_muted, va='center')

# Vertical Down-connector from Pillar 5 (Constitutive Library) into the Bayesian Loop
ax.annotate('', xy=(14.3, 0.87), xytext=(14.3, 1.15),
            arrowprops=dict(arrowstyle="-|>", color=c_gold, lw=2.2, mutation_scale=12))
ax.text(14.3, 1.01, "Uncertainty Feedback", fontsize=6.8, fontweight='bold',
        color=c_navy, ha='center', va='center',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='white', edgecolor=c_gold, lw=0.8))

# Vertical Up-connector from the Bayesian Loop into Pillar 1 (Robotic Loading)
ax.annotate('', xy=(1.725, 1.15), xytext=(1.725, 0.87),
            arrowprops=dict(arrowstyle="-|>", color=c_gold, lw=2.2, mutation_scale=12))
ax.text(1.725, 1.01, "Next Test Command", fontsize=6.8, fontweight='bold',
        color=c_navy, ha='center', va='center',
        bbox=dict(boxstyle="round,pad=0.15", facecolor='white', edgecolor=c_gold, lw=0.8))

plt.tight_layout()
plt.savefig('images/automation_concept.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Successfully regenerated images/automation_concept.png with clean closed-loop connectors")
