import os
import shutil
import re

brain_dir = r'C:\Users\gauri\.gemini\antigravity-ide\brain\5e787bc8-9f13-4eae-889e-047c54323227'
proj_dir = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj'
assets_dir = os.path.join(proj_dir, 'assets')

# Copy images
import glob
idol_img = glob.glob(os.path.join(brain_dir, 'silver_idol_*.png'))[-1]
uten_img = glob.glob(os.path.join(brain_dir, 'silver_utensils_*.png'))[-1]
deco_img = glob.glob(os.path.join(brain_dir, 'silver_decor_*.png'))[-1]

shutil.copy(idol_img, os.path.join(assets_dir, 'silver_idol_new.png'))
shutil.copy(uten_img, os.path.join(assets_dir, 'silver_utensils_new.png'))
shutil.copy(deco_img, os.path.join(assets_dir, 'silver_decor_new.png'))

html_path = os.path.join(proj_dir, 'silver-artifacts.html')
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the top-styles-section and everything inside it with the new layout
new_html = r'''
        <section class="artifacts-intro" style="background-color: #faf9f6; padding: 4rem 5%; text-align: center;">
            <h1 style="font-family: var(--font-heading); font-size: 3rem; margin-bottom: 1rem; color: #1a1a1a; font-weight: 400;">Pure Silver <span style="font-style: italic;">Masterpieces</span></h1>
            <p style="font-size: 1.1rem; color: #666; max-width: 600px; margin: 0 auto; line-height: 1.6;">Discover our range of exquisite silver articles, from divine idols to heritage utensils.</p>
            <div style="width: 6px; height: 6px; background-color: #cda975; border-radius: 50%; margin: 2rem auto 0;"></div>
        </section>

        <section class="artifact-showcase" style="padding: 5rem 10%; background-color: #fff;">
            <style>
                @media (max-width: 900px) {
                    .artifact-block { flex-direction: column !important; text-align: center; }
                    .artifact-block.reverse { flex-direction: column !important; }
                    .artifact-text { padding: 2rem 0 !important; }
                }
            </style>
            
            <!-- Block 1 -->
            <div class="artifact-block" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8rem; gap: 4rem;">
                <div class="artifact-img" style="flex: 1;">
                    <img src="assets/silver_idol_new.png" alt="Divine Silver Idols" style="width: 100%; height: auto; object-fit: cover;">
                </div>
                <div class="artifact-text" style="flex: 1; padding: 2rem;">
                    <h2 style="font-family: var(--font-heading); font-size: 2.5rem; margin-bottom: 1.5rem; color: #1a1a1a; font-weight: 400;">Divine Silver Idols</h2>
                    <p style="font-size: 1.1rem; color: #666; line-height: 1.8; margin-bottom: 2.5rem;">Pure silver idols crafted with divine precision, perfect for your home temple or as auspicious gifts.</p>
                    <a href="contact.html" class="btn" style="padding: 12px 30px; font-size: 0.8rem; background: transparent; color: #cda975; border: 1px solid #cda975;">INQUIRE FOR CUSTOMIZATION</a>
                </div>
            </div>

            <!-- Block 2 (Reversed) -->
            <div class="artifact-block reverse" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8rem; gap: 4rem; flex-direction: row-reverse;">
                <div class="artifact-img" style="flex: 1;">
                    <img src="assets/silver_utensils_new.png" alt="Heritage Silver Utensils" style="width: 100%; height: auto; object-fit: cover;">
                </div>
                <div class="artifact-text" style="flex: 1; padding: 2rem;">
                    <h2 style="font-family: var(--font-heading); font-size: 2.5rem; margin-bottom: 1.5rem; color: #1a1a1a; font-weight: 400;">Heritage Silver Utensils</h2>
                    <p style="font-size: 1.1rem; color: #666; line-height: 1.8; margin-bottom: 2.5rem;">Traditional silver dinnerware and utensils, combining health benefits with timeless luxury.</p>
                    <a href="contact.html" class="btn" style="padding: 12px 30px; font-size: 0.8rem; background: transparent; color: #cda975; border: 1px solid #cda975;">INQUIRE FOR CUSTOMIZATION</a>
                </div>
            </div>

            <!-- Block 3 -->
            <div class="artifact-block" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4rem; gap: 4rem;">
                <div class="artifact-img" style="flex: 1;">
                    <img src="assets/silver_decor_new.png" alt="Exclusive Silver Decor" style="width: 100%; height: auto; object-fit: cover;">
                </div>
                <div class="artifact-text" style="flex: 1; padding: 2rem;">
                    <h2 style="font-family: var(--font-heading); font-size: 2.5rem; margin-bottom: 1.5rem; color: #1a1a1a; font-weight: 400;">Exclusive Silver Decor</h2>
                    <p style="font-size: 1.1rem; color: #666; line-height: 1.8; margin-bottom: 2.5rem;">Modern and traditional silver decorative pieces to add a touch of regality to your living space.</p>
                    <a href="contact.html" class="btn" style="padding: 12px 30px; font-size: 0.8rem; background: transparent; color: #cda975; border: 1px solid #cda975;">INQUIRE FOR CUSTOMIZATION</a>
                </div>
            </div>
        </section>
'''

# Use regex to replace the existing top-styles-section
content = re.sub(r'<section class="top-styles-section".*?</section>', new_html, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated silver-artifacts.html')
