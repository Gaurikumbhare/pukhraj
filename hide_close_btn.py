import os

directory = r"c:\Users\gauri\OneDrive\Desktop\jweller"

css_to_add = """
@media (min-width: 769px) {
    .close-menu-btn { display: none !important; }
    .nav-accordion-item { display: none !important; }
}
"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        
        # Check if the file has a <style> tag
        if '<style>' in content and css_to_add.strip() not in content:
            content = content.replace('</style>', css_to_add + '</style>', 1)
            updated = True
        elif '<style>' not in content and '</head>' in content:
            content = content.replace('</head>', '<style>' + css_to_add + '</style></head>', 1)
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
