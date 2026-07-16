import glob
import os
import re

directory = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj'
files = glob.glob(os.path.join(directory, '*.html'))

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Contact Us to navbar, if it's not already there
    if '<li><a href="contact.html">Contact Us</a></li>' not in content:
        new_content = re.sub(
            r'(<li class="nav-has-badge"><span class="nav-badge red-badge">New</span><a href="pop\.html">POP</a></li>)',
            r'\1\n                <li><a href="contact.html">Contact Us</a></li>',
            content
        )

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {os.path.basename(file_path)}')
