import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the category-circles-section
content = re.sub(r'<!-- Everyday Demifine Jewellery \(Categories\) -->.*?</section>\s*<!-- Top Styles \(Bestsellers with filters\) -->', '<!-- Top Styles (Bestsellers with filters) -->', content, flags=re.DOTALL)

# 2. Add filter menu to Top Styles
filter_html = '''
            <div class="filter-menu-container">
                <button class="filter-btn active">ALL</button>
                <button class="filter-btn">NECKLACES</button>
                <button class="filter-btn">BRACELETS</button>
                <button class="filter-btn">EARRINGS</button>
                <button class="filter-btn">RINGS</button>
                <button class="filter-btn">MENS</button>
                <button class="filter-btn">MANGALSUTRA</button>
            </div>
'''
content = re.sub(r'(<h2.*?Pukhraj Top Styles</h2>)', r'\1\n' + filter_html, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
