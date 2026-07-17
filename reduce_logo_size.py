import glob
import re

target_pattern = r'<img\s+src=\"assets/image copy 40\.png\"\s+alt=\"Pukhraj Logo\"\s+style=\"width:\s*140px;\s*height:\s*auto;\s*object-fit:\s*contain;\s*mix-blend-mode:\s*screen;\">'

replacement = '<img src="assets/image copy 40.png" alt="Pukhraj Logo" style="width: 90px; height: auto; object-fit: contain; mix-blend-mode: screen;">'

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content, count = re.subn(target_pattern, replacement, content, flags=re.DOTALL)
    
    if count > 0 and new_content != content:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(file_name)
        
print('Updated logo size to 90px in:', ', '.join(updated_files))
