import re
import os

filepath = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj\silver-artifacts.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """
        <section class="artifact-showcase-light" style="padding: 5rem 10%; background-color: #fdfaf5; color: #1a1a1a;">
            <style>
                .artifact-row {
                    display: flex;
                    align-items: center;
                    gap: 6rem;
                    margin-bottom: 8rem;
                }
                .artifact-row.reverse {
                    flex-direction: row-reverse;
                }
                .artifact-img-wrap {
                    flex: 1;
                    position: relative;
                }
                .artifact-img-wrap img {
                    width: 100%;
                    height: auto;
                    display: block;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
                }
                .artifact-img-badge {
                    position: absolute;
                    top: 20px;
                    left: 20px;
                    background: rgba(0,0,0,0.65);
                    padding: 8px 12px;
                    color: #fff;
                    font-size: 0.6rem;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    font-family: monospace;
                    line-height: 1.4;
                }
                .artifact-img-badge span {
                    color: #cda975;
                }
                .artifact-img-badge-right {
                    position: absolute;
                    bottom: 20px;
                    right: 20px;
                    background: rgba(0,0,0,0.65);
                    padding: 8px 12px;
                    color: #fff;
                    font-size: 0.6rem;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    font-family: monospace;
                    line-height: 1.4;
                    text-align: right;
                }
                .artifact-img-badge-right span {
                    color: #cda975;
                }
                .artifact-text-wrap {
                    flex: 1;
                }
                .artifact-overline {
                    font-size: 0.75rem;
                    color: #cda975;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    margin-bottom: 1rem;
                    font-weight: 600;
                }
                .artifact-title-light {
                    font-family: var(--font-heading);
                    font-size: 2.5rem;
                    font-weight: 400;
                    color: #333;
                    margin-bottom: 1.5rem;
                }
                .artifact-desc-light {
                    font-size: 0.95rem;
                    line-height: 1.8;
                    color: #666;
                    margin-bottom: 2.5rem;
                }
                .artifact-link-1 {
                    display: inline-block;
                    font-size: 0.75rem;
                    font-weight: 700;
                    color: #555;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    text-decoration: none;
                    border-bottom: 2px solid #ddd;
                    padding-bottom: 4px;
                    margin-bottom: 1.5rem;
                    transition: border-color 0.3s;
                }
                .artifact-link-1:hover {
                    border-color: #555;
                }
                .artifact-link-2 {
                    display: block;
                    font-size: 0.75rem;
                    font-weight: 700;
                    color: #cda975;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    text-decoration: none;
                }
                
                @media (max-width: 900px) {
                    .artifact-row { flex-direction: column !important; gap: 3rem; margin-bottom: 5rem; }
                }
            </style>
            
            <!-- Row 1 -->
            <div class="artifact-row">
                <div class="artifact-img-wrap">
                    <img src="assets/silver_idol_new.png" alt="Divine Silver Idols">
                    <div class="artifact-img-badge">
                        ARCHIVAL RECORD ID: 082-SLV<br>
                        <span>CRAFTSMANSHIP SERIES: SACRED</span>
                    </div>
                </div>
                <div class="artifact-text-wrap">
                    <div class="artifact-overline">- SILVER PURITY: 925 STELLAR</div>
                    <h2 class="artifact-title-light">Divine Silver Idols</h2>
                    <p class="artifact-desc-light">Pure silver idols crafted with divine precision, perfect for your home temple or as auspicious gifts. Each piece is hand-burnished to achieve a lunar glow that transcends generations.</p>
                    <a href="contact.html" class="artifact-link-1">INQUIRE FOR CUSTOMIZATION</a>
                    <a href="#" class="artifact-link-2">DISCOVER NARRATIVE &rarr;</a>
                </div>
            </div>

            <!-- Row 2 -->
            <div class="artifact-row reverse">
                <div class="artifact-img-wrap">
                    <img src="assets/silver_utensils_new.png" alt="Heritage Silver Utensils">
                    <div class="artifact-img-badge-right">
                        COLLECTION: THE FEAST<br>
                        <span>WEIGHT: VARIES BY SET</span>
                    </div>
                </div>
                <div class="artifact-text-wrap">
                    <div class="artifact-overline">- ARCHIVAL CURATION</div>
                    <h2 class="artifact-title-light">Heritage Silver Utensils</h2>
                    <p class="artifact-desc-light">Traditional silver dinnerware and utensils, combining health benefits with timeless luxury. Designed for those who treat dining as a sacred ritual of gathering and legacy.</p>
                    <a href="contact.html" class="artifact-link-1">INQUIRE FOR CUSTOMIZATION</a>
                    <a href="#" class="artifact-link-2">EXPLORE THE SET &rarr;</a>
                </div>
            </div>

            <!-- Row 3 -->
            <div class="artifact-row">
                <div class="artifact-img-wrap">
                    <img src="assets/silver_decor_new.png" alt="Exclusive Silver Decor">
                </div>
                <div class="artifact-text-wrap">
                    <div class="artifact-overline">- MODERN HEIRLOOM</div>
                    <h2 class="artifact-title-light">Exclusive Silver Decor</h2>
                    <p class="artifact-desc-light">Modern and traditional silver decorative pieces to add a touch of regality to your living space. Each object is a statement of permanence in an era of transience.</p>
                    <a href="contact.html" class="artifact-link-1">INQUIRE FOR CUSTOMIZATION</a>
                    <a href="#" class="artifact-link-2">CURATE MY SPACE &rarr;</a>
                </div>
            </div>
        </section>
"""

start_marker = '<section class="artifact-showcase-dark"'
end_marker = '</section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if start_idx != -1 and end_idx != -1:
    new_page = content[:start_idx] + new_html.strip() + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_page)
    print("Replaced artifact section with light theme")
else:
    print("Could not find section")
