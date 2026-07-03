import re

with open("collection.html", "r", encoding="utf-8") as f:
    content = f.read()

filter_menu = '''
            <div class="filter-menu-container" style="margin-bottom: 3rem !important; margin-top: 1.5rem !important;">
                <button class="filter-btn active" data-filter="all">ALL</button>
                <button class="filter-btn" data-filter="necklaces">NECKLACES</button>
                <button class="filter-btn" data-filter="bracelets">BRACELETS</button>
                <button class="filter-btn" data-filter="earrings">EARRINGS</button>
                <button class="filter-btn" data-filter="rings">RINGS</button>
                <button class="filter-btn" data-filter="mens">MENS</button>
                <button class="filter-btn" data-filter="mangalsutras">MANGALSUTRA</button>
            </div>
'''

# Insert above product-grid-4
content = content.replace('<div class="product-grid-4">', filter_menu + '\n            <div class="product-grid-4">')

with open("collection.html", "w", encoding="utf-8") as f:
    f.write(content)
