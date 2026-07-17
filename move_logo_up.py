import glob

old_div = '<div style="text-align: center; margin-bottom: -0.5rem; margin-top: 1rem;">'
new_div = '<div style="text-align: center; margin-bottom: -0.5rem; margin-top: -1.5rem;">'

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_div in content:
        new_content = content.replace(old_div, new_div)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(file_name)
        
print('Moved logo section up in:', ', '.join(updated_files))
