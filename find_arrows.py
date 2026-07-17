import re
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<button' in line or '<a' in line:
        if 'left' in line or 'right' in line or 'prev' in line or 'next' in line:
            if 'absolute' in line or 'transform' in line:
                print(f"Line {i}: {line.strip()}")
