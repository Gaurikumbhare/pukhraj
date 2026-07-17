import glob

old_str = 'src="assets/image copy 8.png"'
new_str = 'src="assets/image copy 40.png"'

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_str in content:
        new_content = content.replace(old_str, new_str)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(file_name)
        
print('Replaced image 8 with image 40 in:', ', '.join(updated_files))
