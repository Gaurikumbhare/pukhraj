import os
import re

filepath = r"c:\Users\gauri\OneDrive\Desktop\jweller\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'<a href="new-arrivals.html"([^>]*>\s*<img[^>]*alt="Gifts For Her")',
    r'<a href="collection.html?filter=her"\1',
    content
)

content = re.sub(
    r'<a href="new-arrivals.html"([^>]*>\s*<img[^>]*alt="Gifts For Him")',
    r'<a href="collection.html?filter=him"\1',
    content
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated via regex.")
