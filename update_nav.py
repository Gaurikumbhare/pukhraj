import glob
import os
import re

directory = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj'
files = glob.glob(os.path.join(directory, '*.html'))

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Contact Us to navbar
    new_content = re.sub(
        r'(<li><a href="pop\.html">POP</a></li>)',
        r'\1\n                <li><a href="contact.html">Contact Us</a></li>',
        content
    )

    # 2. Make search icon visible
    new_content = re.sub(
        r'<a href="#" class="icon-btn-new mobile-search-icon" title="Search" style="display: none;">',
        r'<a href="#" class="icon-btn-new search-icon" title="Search">',
        new_content
    )

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {os.path.basename(file_path)}')
