import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageChops
import numpy as np

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

fig = plt.figure(figsize=(15.0, 5.0), dpi=300)
gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.25], hspace=0.38)

# ==========================================
# (a) Full Bar Assembly Schematic
# ==========================================
ax1 = fig.add_subplot(gs[0])
ax1.set_xlim(-120, 2260)
ax1.set_ylim(-35, 45)
ax1.axis('off')

# Title
ax1.text(-110, 36, '(a) Full Miniature Kolsky Bar Assembly (Abaqus/Explicit FE Model)', 
         fontsize=11.5, fontweight='bold', color='#0B2545', ha='left', va='center')

bar_h = 16
y_bar = -bar_h / 2

# Striker Bar
striker_w = 95
striker_x = -110
rect_striker = patches.Rectangle((striker_x, y_bar), striker_w, bar_h, 
                                 linewidth=1.3, edgecolor='#0B2545', facecolor='#AED6F1', zorder=2)
ax1.add_patch(rect_striker)
for dx in np.linspace(striker_x, striker_x + striker_w, 6):
    ax1.plot([dx, dx], [y_bar, y_bar + bar_h], color='#1F4E8C', lw=0.6, alpha=0.5, zorder=3)
ax1.text(striker_x + striker_w/2, 0, 'Striker', fontsize=9, fontweight='bold', color='#0B2545', ha='center', va='center', zorder=4)

# Velocity arrow
arrow_end_x = striker_x + striker_w + 14
arrow_start_x = striker_x + striker_w - 16
ax1.annotate('', xy=(arrow_end_x, 0), xytext=(arrow_start_x, 0),
             arrowprops=dict(arrowstyle='->,head_width=0.4,head_length=0.5', lw=2.2, color='#D49B28'), zorder=5)
ax1.text(striker_x + striker_w + 3, 14, r'$V_0 = 12.4\ \mathrm{m/s}$', fontsize=9, fontweight='bold', color='#B78103', ha='center', va='bottom')

# Pulse Shaper
shaper_x = striker_x + striker_w + 24
shaper_w = 12
rect_shaper = patches.Rectangle((shaper_x, y_bar + 2), shaper_w, bar_h - 4, 
                                linewidth=1.1, edgecolor='#935116', facecolor='#EDBB99', zorder=4)
ax1.add_patch(rect_shaper)
ax1.annotate('Pulse\nShaper', xy=(shaper_x + shaper_w/2, -bar_h/2), xytext=(shaper_x + shaper_w/2, -26),
             arrowprops=dict(arrowstyle='->', lw=1.1, color='#935116'),
             fontsize=8, fontweight='bold', color='#935116', ha='center', va='top')

# Incident Bar
inc_x = shaper_x + shaper_w + 6
inc_w = 950
rect_inc = patches.Rectangle((inc_x, y_bar), inc_w, bar_h, 
                             linewidth=1.3, edgecolor='#0B2545', facecolor='#E8F8F5', zorder=2)
ax1.add_patch(rect_inc)
for dx in np.linspace(inc_x, inc_x + inc_w, 28):
    ax1.plot([dx, dx], [y_bar, y_bar + bar_h], color='#117A65', lw=0.4, alpha=0.4, zorder=3)
ax1.text(inc_x + inc_w * 0.45, 0, r'Incident Bar  ($L_i = 1000\ \mathrm{mm},\ \varnothing 3.17\ \mathrm{mm}$)', 
         fontsize=9, fontweight='bold', color='#0B2545', ha='center', va='center', zorder=4)

# Strain Gauge 1
sg1_x = inc_x + inc_w / 2
rect_sg1 = patches.Rectangle((sg1_x - 14, bar_h/2), 28, 5, 
                             linewidth=1.1, edgecolor='#B7950B', facecolor='#F9E79F', zorder=5)
ax1.add_patch(rect_sg1)
ax1.text(sg1_x, bar_h/2 + 6, r'SG 1 ($L_i / 2$)', fontsize=8.5, fontweight='bold', color='#7D6608', ha='center', va='bottom')

# Specimen
spec_x = inc_x + inc_w + 8
spec_w = 26
rect_spec = patches.Rectangle((spec_x, y_bar + 1.5), spec_w, bar_h - 3,
                              linewidth=1.3, edgecolor='#922B21', facecolor='#FADBD8', zorder=4)
ax1.add_patch(rect_spec)
ax1.text(spec_x + spec_w/2, bar_h/2 + 15, 'Specimen', fontsize=9, fontweight='bold', color='#922B21', ha='center', va='bottom')

# Zoom Callout Box
zoom_box = patches.Rectangle((spec_x - 18, -bar_h - 5), spec_w + 36, bar_h*2 + 10,
                             linewidth=1.5, edgecolor='#C0392B', facecolor='none', linestyle='--', zorder=6)
ax1.add_patch(zoom_box)
ax1.text(spec_x + spec_w/2, -bar_h - 9, 'ZOOM', fontsize=8.5, fontweight='bold', color='#C0392B', ha='center', va='top')

# Transmission Bar
trans_x = spec_x + spec_w + 8
trans_w = 950
rect_trans = patches.Rectangle((trans_x, y_bar), trans_w, bar_h,
                               linewidth=1.3, edgecolor='#0B2545', facecolor='#E8F8F5', zorder=2)
ax1.add_patch(rect_trans)
for dx in np.linspace(trans_x, trans_x + trans_w, 28):
    ax1.plot([dx, dx], [y_bar, y_bar + bar_h], color='#117A65', lw=0.4, alpha=0.4, zorder=3)
ax1.text(trans_x + trans_w * 0.52, 0, r'Transmission Bar  ($L_t = 1000\ \mathrm{mm},\ \varnothing 3.17\ \mathrm{mm}$)', 
         fontsize=9, fontweight='bold', color='#0B2545', ha='center', va='center', zorder=4)

# Strain Gauge 2
sg2_x = trans_x + trans_w / 2
rect_sg2 = patches.Rectangle((sg2_x - 14, bar_h/2), 28, 5, 
                             linewidth=1.1, edgecolor='#B7950B', facecolor='#F9E79F', zorder=5)
ax1.add_patch(rect_sg2)
ax1.text(sg2_x, bar_h/2 + 6, r'SG 2 ($L_t / 2$)', fontsize=8.5, fontweight='bold', color='#7D6608', ha='center', va='bottom')

# Rigid Stop / Boundary Support
rigid_x = trans_x + trans_w
ax1.plot([rigid_x, rigid_x], [y_bar - 10, y_bar + bar_h + 10], color='#2C3E50', lw=3.0, zorder=5)
for hy in np.linspace(y_bar - 10, y_bar + bar_h + 4, 7):
    ax1.plot([rigid_x, rigid_x + 16], [hy, hy + 8], color='#2C3E50', lw=1.3, zorder=5)
ax1.text(rigid_x + 22, 0, 'Rigid Stop', fontsize=8.5, fontweight='bold', color='#555555', ha='left', va='center')


# ==========================================
# (b) Zoom: Specimen Interface Mesh
# ==========================================
ax2 = fig.add_subplot(gs[1])
im_mesh = Image.open('images/kolskyimage.png')
w_m, h_m = im_mesh.size
im_mesh_cropped = im_mesh.crop((20, 10, w_m - 20, h_m - 10))

ax2.imshow(im_mesh_cropped)
ax2.set_title('(b) Detail: Specimen Interface Mesh (Abaqus/Explicit Quarter-Symmetric C3D8R Hex Elements)', 
              fontsize=11, fontweight='bold', color='#0B2545', pad=5)
ax2.axis('off')

for spine in ax2.spines.values():
    spine.set_visible(True)
    spine.set_color('#1F4E8C')
    spine.set_linewidth(1.0)

plt.subplots_adjust(left=0.01, right=0.99, top=0.94, bottom=0.03)

# Save and crop
temp_path = 'images/digital_twin_full_and_zoom.png'
plt.savefig(temp_path, bbox_inches='tight', dpi=300, facecolor='white')

# Tight autocrop
im_temp = Image.open(temp_path).convert('RGB')
bg = Image.new('RGB', im_temp.size, (255, 255, 255))
diff = ImageChops.difference(im_temp, bg)
bbox = diff.getbbox()
pad = 12
crop_box = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(im_temp.width, bbox[2]+pad), min(im_temp.height, bbox[3]+pad))
im_temp.crop(crop_box).save(temp_path)
print('Optimized digital_twin_full_and_zoom.png created!')
