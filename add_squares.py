import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

square_html = '''
            <div class="square-categories">
                <a href="earrings.html" class="square-category-item">
                    <div class="square-img" style="background-image: url('assets/gold_earrings.png');"></div>
                    <span>Earrings</span>
                </a>
                <a href="necklaces.html" class="square-category-item">
                    <div class="square-img" style="background-image: url('assets/silver_necklace.png');"></div>
                    <span>Necklaces</span>
                </a>
                <a href="bracelets.html" class="square-category-item">
                    <div class="square-img" style="background-image: url('assets/indian_gold_bangles.png');"></div>
                    <span>Bracelets</span>
                </a>
                <a href="rings.html" class="square-category-item">
                    <div class="square-img" style="background-image: url('assets/gold_rings.png');"></div>
                    <span>Rings</span>
                </a>
                <a href="new-arrivals.html" class="square-category-item">
                    <div class="square-img" style="background-image: url('assets/station_mangalsutra.png');"></div>
                    <span>Mangalsutra</span>
                </a>
                <a href="new-arrivals.html" class="square-category-item">
                    <div class="square-img" style="background-image: url('assets/silver_idol.png');"></div>
                    <span>Men</span>
                </a>
            </div>
'''

content = re.sub(r'(<div class="filter-menu-container">.*?</div>)', r'\1\n' + square_html, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
