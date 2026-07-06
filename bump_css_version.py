import os

directory = r"c:\Users\gauri\OneDrive\Desktop\jweller"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        if 'styles.css?v=12' in content:
            content = content.replace('styles.css?v=12', 'styles.css?v=13')
            updated = True
        elif 'styles.css' in content and 'styles.css?v=' not in content:
            content = content.replace('styles.css', 'styles.css?v=13')
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
