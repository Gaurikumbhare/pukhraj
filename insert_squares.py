import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

square_html = '''
            <div class="category-squares" style="display: flex; gap: 1.5rem; justify-content: center; margin-bottom: 2rem; flex-wrap: wrap;">
                <a href="earrings.html" class="category-square-item" style="text-align: center; text-decoration: none; color: #333;">
                    <div class="square-img" style="width: 120px; height: 120px; background-image: url('assets/gold_earrings.png'); background-size: cover; background-position: center; margin-bottom: 0.5rem; border-radius: 4px;"></div>
                    <span style="font-size: 0.85rem; font-weight: 500;">Earrings</span>
                </a>
                <a href="necklaces.html" class="category-square-item" style="text-align: center; text-decoration: none; color: #333;">
                    <div class="square-img" style="width: 120px; height: 120px; background-image: url('assets/silver_necklace.png'); background-size: cover; background-position: center; margin-bottom: 0.5rem; border-radius: 4px;"></div>
                    <span style="font-size: 0.85rem; font-weight: 500;">Necklaces</span>
                </a>
                <a href="bracelets.html" class="category-square-item" style="text-align: center; text-decoration: none; color: #333;">
                    <div class="square-img" style="width: 120px; height: 120px; background-image: url('assets/indian_gold_bangles.png'); background-size: cover; background-position: center; margin-bottom: 0.5rem; border-radius: 4px;"></div>
                    <span style="font-size: 0.85rem; font-weight: 500;">Bracelets</span>
                </a>
                <a href="rings.html" class="category-square-item" style="text-align: center; text-decoration: none; color: #333;">
                    <div class="square-img" style="width: 120px; height: 120px; background-image: url('assets/gold_rings.png'); background-size: cover; background-position: center; margin-bottom: 0.5rem; border-radius: 4px;"></div>
                    <span style="font-size: 0.85rem; font-weight: 500;">Rings</span>
                </a>
                <a href="new-arrivals.html" class="category-square-item" style="text-align: center; text-decoration: none; color: #333;">
                    <div class="square-img" style="width: 120px; height: 120px; background-image: url('assets/station_mangalsutra.png'); background-size: cover; background-position: center; margin-bottom: 0.5rem; border-radius: 4px;"></div>
                    <span style="font-size: 0.85rem; font-weight: 500;">Mangalsutra</span>
                </a>
                <a href="new-arrivals.html" class="category-square-item" style="text-align: center; text-decoration: none; color: #333;">
                    <div class="square-img" style="width: 120px; height: 120px; background-image: url('assets/silver_idol.png'); background-size: cover; background-position: center; margin-bottom: 0.5rem; border-radius: 4px;"></div>
                    <span style="font-size: 0.85rem; font-weight: 500;">Men</span>
                </a>
            </div>
'''

content = re.sub(r'(<h2.*?Pukhraj Top Styles</h2>)', r'\1\n' + square_html, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
