import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load PMMA overlay and SEM/CT images
pmma_img = Image.open('images/pmma_overlay.png')
imaging_img = Image.open('images/Imaging.png')

# Crops from Imaging.png:
# sem2: fiber shear kinking (360, 12, 700, 275)
# ct: 3D micro-ct volumetric scan (5, 285, 528, 685)
sem2 = imaging_img.crop((360, 12, 700, 275))
ct = imaging_img.crop((5, 285, 528, 685))

# Create a clean composite figure with larger height and clear typography
fig = plt.figure(figsize=(15.5, 4.8), dpi=300)
fig.patch.set_facecolor('white')

# Grid: Left = PMMA plot, Middle = SEM, Right = Micro-CT
gs = fig.add_gridspec(1, 3, width_ratios=[1.42, 0.96, 1.02], wspace=0.15,
                       left=0.015, right=0.985, top=0.88, bottom=0.04)

ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])

# Left: PMMA Rate-Dependent Response
ax1.imshow(pmma_img)
ax1.set_title('(a) Rate-Dependent Dynamic Stress vs. Strain', fontsize=11.5, fontweight='bold', color='#0B2545', pad=7)
ax1.axis('off')
for spine in ax1.spines.values():
    spine.set_visible(True)
    spine.set_color('#1F4E8C')
    spine.set_linewidth(1.2)

# Middle: SEM Shear Kinking
ax2.imshow(sem2)
ax2.set_title('(b) SEM: Fiber Shear Kinking', fontsize=11.5, fontweight='bold', color='#0B2545', pad=7)
ax2.axis('off')
for spine in ax2.spines.values():
    spine.set_visible(True)
    spine.set_color('#1F4E8C')
    spine.set_linewidth(1.2)

# Right: Micro-CT Volumetric Scan
ax3.imshow(ct)
ax3.set_title('(c) 3D Micro-CT Volumetric Damage', fontsize=11.5, fontweight='bold', color='#0B2545', pad=7)
ax3.axis('off')
for spine in ax3.spines.values():
    spine.set_visible(True)
    spine.set_color('#1F4E8C')
    spine.set_linewidth(1.2)

plt.savefig('images/rate_and_damage_composite.png', dpi=300, bbox_inches='tight', facecolor='white')
print('Successfully re-generated images/rate_and_damage_composite.png')
