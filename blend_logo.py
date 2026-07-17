import glob

old_str = '<img src="assets/image copy 8.png" alt="Pukhraj Logo" style="width: 70px; height: auto; object-fit: contain; border-radius: 4px;">'
new_str = '<img src="assets/image copy 8.png" alt="Pukhraj Logo" style="width: 70px; height: auto; object-fit: contain; border-radius: 4px; mix-blend-mode: screen;">'

# Wait, earlier I decided lighten, but let's just use screen, which removes dark backgrounds nicely.
# Or 'lighten'. Either works well for white/gold logos on black.

updated_files = []
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_str in content:
        new_content = content.replace(old_str, new_str)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(file_name)
        
print('Blended footer logo in:', ', '.join(updated_files))
