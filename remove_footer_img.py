import glob
import re

target_pattern = r'<div\s+style=\"text-align:\s*center;\s*margin-bottom:\s*1rem;\">\s*<img\s+src=\"assets/acp-elevation-sign-board-1000x1000.webp\"[^>]*>\s*</div>'

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content, count = re.subn(target_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    if count > 0 and new_content != content:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(file_name)
        
print('Removed footer logo image in:', ', '.join(updated_files))
