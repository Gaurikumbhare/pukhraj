import os
import re

directory = r"c:\Users\gauri\OneDrive\Desktop\jweller"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to remove the <li class="nav-accordion-item ... </li> block completely
        # Since it's multi-line, we'll use regex.
        pattern = r'<li class="nav-accordion-item.*?</li>'
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, '', content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed from {filename}")
