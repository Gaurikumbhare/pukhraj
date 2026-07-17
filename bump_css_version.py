import glob
import re
import time

new_version = int(time.time())

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={new_version}', content)
    content = re.sub(r'script\.js\?v=\d+', f'script.js?v={new_version}', content)
    # Just in case script.js doesn't have a ?v= yet:
    content = re.sub(r'src="script\.js"', f'src="script.js?v={new_version}"', content)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    updated_files.append(file_name)
        
print('Bumped styles.css and script.js version in:', ', '.join(updated_files))
