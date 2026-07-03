import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the buttons
content = re.sub(r'\s*<button class="add-to-bag-btn">ADD TO BAG</button>', '', content)

# Remove the injected style block
content = re.sub(r'<style>\s*\.add-to-bag-btn\s*\{.*?</style>', '', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
