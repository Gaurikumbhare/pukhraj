import re
import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # The category-squares div ends where the next section or grid begins.
    # Let's use a regex to find <div class="category-squares"... and remove it entirely
    # up to the <div class="product-grid-4">
    
    # We can match <div class="category-squares" ... </div> before <div class="product-grid-4">
    # Because of nested divs inside category-squares, regex with non-greedy might be tricky.
    # Actually, we can just match from <div class="category-squares" to </a>\s*</div> right before product-grid-4
    
    pattern = re.compile(r'<div class="category-squares".*?</a>\s*</div>', re.DOTALL)
    new_content = pattern.sub('', content)

    if new_content != content:
        print(f"Updated {file}")
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
