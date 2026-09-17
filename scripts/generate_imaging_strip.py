import matplotlib.pyplot as plt
from PIL import Image, ImageChops

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

im = Image.open('images/Imaging.png')

# Precise sub-image crops
sem1 = im.crop((12, 12, 360, 275))
sem2 = im.crop((360, 12, 700, 275))
sem3 = im.crop((700, 12, 1055, 275))
ct = im.crop((5, 285, 528, 685))
debris = im.crop((532, 285, 1055, 685))

panels = [
    (sem1, '(a) SEM: Intact Profile'),
    (sem2, '(b) SEM: Fiber Shear Kinking'),
    (sem3, '(c) SEM: Crushing & Spall'),
    (ct, '(d) 3D Micro-CT Volumetric Scan'),
    (debris, '(e) Void & Debris Analysis')
]

target_h = 400
resized_panels = []
for img, title in panels:
    w = int(img.width * (target_h / img.height))
    r_img = img.resize((w, target_h), Image.Resampling.LANCZOS)
    resized_panels.append((r_img, title, w))

total_w = sum(p[2] for p in resized_panels)
width_ratios = [p[2] for p in resized_panels]

fig, axes = plt.subplots(1, 5, figsize=(16.0, 4.2), dpi=300, gridspec_kw={'width_ratios': width_ratios})

for idx, (img, title, _) in enumerate(resized_panels):
    axes[idx].imshow(img)
    axes[idx].set_title(title, fontsize=8.5, fontweight='bold', color='#0B2545', pad=5)
    axes[idx].axis('off')
    # add subtle border
    for spine in axes[idx].spines.values():
        spine.set_visible(True)
        spine.set_color('#1F4E8C')
        spine.set_linewidth(0.8)

plt.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.03, wspace=0.10)
plt.savefig('images/imaging_wide_strip.png', bbox_inches='tight', dpi=300, facecolor='white')
print('imaging_wide_strip.png successfully created!')
