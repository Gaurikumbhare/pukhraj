import os

menu_toggle = """<div class="menu-toggle" id="mobile-menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            </div>
            <div class="logo-new">PUKHRAJ</div>"""

close_btn = """<ul class="nav-links-new">
                <button class="close-menu-btn">&times;</button>"""

directory = r"c:\Users\gauri\OneDrive\Desktop\jweller"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        if 'id="mobile-menu"' not in content and '<div class="logo-new">PUKHRAJ</div>' in content:
            content = content.replace('<div class="logo-new">PUKHRAJ</div>', menu_toggle)
            content = content.replace('<ul class="nav-links-new">', close_btn)
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
