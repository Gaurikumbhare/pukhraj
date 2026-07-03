import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace filter buttons with data-filter attributes
new_btns = '''
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

content = re.sub(r'<div class="filter-menu-container".*?</div>', new_btns.strip(), content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
