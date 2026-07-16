import os
import glob
import re

directory = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj'
old_name = os.path.join(directory, 'owners-favourite.html')
new_name = os.path.join(directory, 'silver-artifacts.html')
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print('Renamed file to silver-artifacts.html')

with open(os.path.join(directory, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL | re.IGNORECASE)
if not footer_match:
    print('Could not find footer in index.html')
    exit(1)

new_footer = footer_match.group(1)
# Update the footer links to match the navbar
# Remove 'Fine Silver' and change 'Owner's Favourite' to 'Silver Artifacts'
new_footer = re.sub(r'<li><a href="9kt-fine-silver\.html"><span class="arr">&gt;</span> Fine Silver</a></li>\s*', '', new_footer)
new_footer = new_footer.replace("Owner's Favourite", "Silver Artifacts")
new_footer = new_footer.replace("Owner&#39;s Favourite", "Silver Artifacts")
new_footer = new_footer.replace("owners-favourite.html", "silver-artifacts.html")

html_files = glob.glob(os.path.join(directory, '*.html'))
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace footer completely
    content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL | re.IGNORECASE)
    
    # Replace the text 'Owner's Favourite' anywhere else (like navbar, page headers, etc.)
    content = content.replace("Owner's Favourite", "Silver Artifacts")
    content = content.replace("Owner&#39;s Favourite", "Silver Artifacts")
    content = content.replace("owners-favourite.html", "silver-artifacts.html")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated all HTML files successfully!')
