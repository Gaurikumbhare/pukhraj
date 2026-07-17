import glob
import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

nav_match = re.search(r'<nav class="navbar-new".*?</nav>', index_content, flags=re.DOTALL)
if nav_match:
    nav_html = nav_match.group(0)
    
    for file_name in glob.glob('*.html'):
        if file_name == 'index.html':
            continue
            
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, count = re.subn(r'<nav.*?</nav>', nav_html, content, flags=re.DOTALL)
        
        if count > 0 and new_content != content:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print('Updated navbar in:', file_name)
else:
    print('Could not find navbar in index.html')
