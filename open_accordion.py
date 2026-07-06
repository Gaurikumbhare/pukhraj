import os

directory = r"c:\Users\gauri\OneDrive\Desktop\jweller"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        if '<li class="nav-accordion-item">' in content:
            content = content.replace('<li class="nav-accordion-item">', '<li class="nav-accordion-item active">')
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
