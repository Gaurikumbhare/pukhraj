import os
import glob
import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

nav_match = re.search(r'(<nav class="navbar-new">.*?</nav>)', index_html, re.DOTALL)
if not nav_match:
    print('Nav not found in index.html!')
    exit(1)

nav_content = nav_match.group(1)

html_files = glob.glob('*.html')
html_files.remove('index.html')

updated_count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = re.subn(r'<nav class="navbar-new">.*?</nav>', nav_content.replace('\\', '\\\\'), content, flags=re.DOTALL)
    
    if count > 0 and new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        print(f'Updated {file}')

print(f'Successfully updated nav in {updated_count} files.')
