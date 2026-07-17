import glob
import re

target_str = '<h2 class="footer-logo-title">PUKHRAJ</h2>'
replacement_str = '''<div style="text-align: center; margin-bottom: 1rem;">
                        <img src="assets/image copy 8.png" alt="Pukhraj Logo" style="width: 70px; height: auto; object-fit: contain; border-radius: 4px;">
                    </div>
                    <h2 class="footer-logo-title">PUKHRAJ</h2>'''

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if target_str in content:
        new_content = content.replace(target_str, replacement_str)
        if new_content != content:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.append(file_name)
        
print('Added image 8 to footer in:', ', '.join(updated_files))
