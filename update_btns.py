import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find <button class="wishlist-btn">...</button> and append <button class="add-to-bag-btn">ADD TO BAG</button> right after it.
content = re.sub(r'(<button class="wishlist-btn">.*?</button>)', r'\1\n                        <button class="add-to-bag-btn">ADD TO BAG</button>', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
