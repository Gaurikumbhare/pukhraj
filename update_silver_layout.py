import re
import os

filepath = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj\silver-artifacts.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """
        <section class="artifact-showcase-dark" style="padding: 5rem 10%; background-color: #0b0705; color: #f2efe9;">
            <style>
                .artifact-card-dark {
                    display: flex;
                    align-items: stretch;
                    background-color: #210d0c;
                    border-radius: 16px;
                    overflow: hidden;
                    margin-bottom: 3rem;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                }
                .artifact-card-dark.reverse {
                    flex-direction: row-reverse;
                }
                .artifact-img-dark {
                    flex: 1;
                    min-height: 400px;
                }
                .artifact-img-dark img {
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }
                .artifact-content-dark {
                    flex: 1;
                    padding: 4rem;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                }
                .artifact-number {
                    font-size: 4rem;
                    font-weight: 300;
                    color: rgba(205, 169, 117, 0.2);
                    margin-bottom: 1rem;
                    font-family: var(--font-heading);
                }
                .artifact-title-dark {
                    font-size: 2.2rem;
                    color: #f2efe9;
                    font-family: var(--font-heading);
                    font-weight: 400;
                    margin-bottom: 1rem;
                }
                .artifact-separator {
                    width: 60px;
                    height: 2px;
                    background-color: #cda975;
                    margin-bottom: 1.5rem;
                }
                .artifact-desc-dark {
                    font-size: 1.05rem;
                    color: #d1c9c4;
                    line-height: 1.8;
                    margin-bottom: 3rem;
                }
                .btn-explore-dark {
                    display: inline-flex;
                    align-items: center;
                    justify-content: space-between;
                    padding: 12px 24px;
                    font-size: 0.85rem;
                    color: #cda975;
                    border: 1px solid #cda975;
                    text-decoration: none;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    width: fit-content;
                    transition: all 0.3s;
                }
                .btn-explore-dark:hover {
                    background-color: #cda975;
                    color: #111;
                }
                
                @media (max-width: 900px) {
                    .artifact-card-dark { flex-direction: column !important; }
                    .artifact-img-dark { min-height: 300px; }
                    .artifact-content-dark { padding: 2rem; }
                }
            </style>
            
            <div style="text-align: center; margin-bottom: 4rem;">
                <p style="color: #cda975; text-transform: uppercase; letter-spacing: 3px; font-size: 0.9rem; margin-bottom: 1rem;">OUR COLLECTIONS</p>
                <h2 style="font-family: var(--font-heading); font-size: 3rem; color: #f2efe9; font-weight: 400;">Crafted in Pure Silver</h2>
                <div style="width: 50px; height: 1px; background-color: #cda975; margin: 1.5rem auto 0;"></div>
            </div>
            
            <!-- Card 1 -->
            <div class="artifact-card-dark">
                <div class="artifact-img-dark">
                    <img src="assets/silver_idol_new.png" alt="Divine Silver Idols">
                </div>
                <div class="artifact-content-dark">
                    <div class="artifact-number">01</div>
                    <h3 class="artifact-title-dark">Divine Silver Idols</h3>
                    <div class="artifact-separator"></div>
                    <p class="artifact-desc-dark">Pure silver idols crafted with divine precision, perfect for your home temple or auspicious gifts.</p>
                    <a href="contact.html" class="btn-explore-dark">EXPLORE COLLECTION <span style="margin-left:15px;">&gt;</span></a>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="artifact-card-dark reverse">
                <div class="artifact-img-dark">
                    <img src="assets/silver_utensils_new.png" alt="Heritage Silver Utensils">
                </div>
                <div class="artifact-content-dark">
                    <div class="artifact-number">02</div>
                    <h3 class="artifact-title-dark">Heritage Silver Utensils</h3>
                    <div class="artifact-separator"></div>
                    <p class="artifact-desc-dark">Traditional silver dinnerware and utensils, combining health benefits with timeless luxury.</p>
                    <a href="contact.html" class="btn-explore-dark">EXPLORE COLLECTION <span style="margin-left:15px;">&gt;</span></a>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="artifact-card-dark">
                <div class="artifact-img-dark">
                    <img src="assets/silver_decor_new.png" alt="Exclusive Silver Decor">
                </div>
                <div class="artifact-content-dark">
                    <div class="artifact-number">03</div>
                    <h3 class="artifact-title-dark">Exclusive Silver Decor</h3>
                    <div class="artifact-separator"></div>
                    <p class="artifact-desc-dark">Modern and traditional silver decorative pieces to add a touch of regality to your living space.</p>
                    <a href="contact.html" class="btn-explore-dark">EXPLORE COLLECTION <span style="margin-left:15px;">&gt;</span></a>
                </div>
            </div>
        </section>
"""

start_marker = '<section class="artifact-showcase"'
end_marker = '</section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if start_idx != -1 and end_idx != -1:
    new_page = content[:start_idx] + new_html.strip() + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_page)
    print("Replaced artifact section")
else:
    print("Could not find section")
