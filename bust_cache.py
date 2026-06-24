import os

filepath = r"c:\Users\gauri\OneDrive\Desktop\jweller\collection.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

import random
v = random.randint(100, 999)
content = content.replace('<script src="script.js"></script>', f'<script src="script.js?v={v}"></script>')

# Just in case it already had a version
import re
content = re.sub(r'<script src="script\.js\?v=\d+"></script>', f'<script src="script.js?v={v}"></script>', content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Busted script.js cache with ?v={v}")
