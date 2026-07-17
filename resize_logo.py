import glob

old_str = '<div style="text-align: center; margin-bottom: 1rem;">\n                        <img src="assets/image copy 40.png" alt="Pukhraj Logo" style="width: 70px; height: auto; object-fit: contain; border-radius: 4px; mix-blend-mode: screen;">\n                    </div>'
new_str = '<div style="text-align: center; margin-bottom: 0;">\n                        <img src="assets/image copy 40.png" alt="Pukhraj Logo" style="width: 120px; height: auto; object-fit: contain; mix-blend-mode: screen;">\n                    </div>'

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Since there might be some indentation or newline differences, let's just replace the exact img tag first.
    # Actually, replacing using re to be safe against whitespace variations.
    pass

import re

target_pattern = r'<div\s+style=\"text-align:\s*center;\s*margin-bottom:\s*1rem;\">\s*<img\s+src=\"assets/image copy 40\.png\"\s+alt=\"Pukhraj Logo\"\s+style=\"width:\s*70px;\s*height:\s*auto;\s*object-fit:\s*contain;\s*border-radius:\s*4px;\s*mix-blend-mode:\s*screen;\">\s*</div>'

replacement = '''<div style="text-align: center; margin-bottom: -0.5rem; margin-top: 1rem;">
                        <img src="assets/image copy 40.png" alt="Pukhraj Logo" style="width: 140px; height: auto; object-fit: contain; mix-blend-mode: screen;">
                    </div>'''

for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content, count = re.subn(target_pattern, replacement, content, flags=re.DOTALL)
    
    if count > 0 and new_content != content:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(file_name)
        
print('Updated logo size and position in:', ', '.join(updated_files))
