import os
import glob
import re

directory = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj'
index_path = os.path.join(directory, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

footer_match = re.search(r'(<footer.*?>.*?</footer>)', index_content, re.DOTALL | re.IGNORECASE)
if not footer_match:
    print("Could not find footer in index.html")
    exit(1)
new_footer = footer_match.group(1)

html_files = glob.glob(os.path.join(directory, '*.html'))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace footer
    content = re.sub(r'<footer.*?>.*?</footer>', new_footer, content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove price regular (e.g. <span class="price-regular">₹4,000</span>)
    content = re.sub(r'\s*<span class="price-regular">.*?</span>\s*', ' ', content)
    
    # Remove price discount (e.g. <span class="price-discount">(30% off)</span>)
    content = re.sub(r'\s*<span class="price-discount">.*?</span>\s*', ' ', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files with new footer and cleaned up prices.")
