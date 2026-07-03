import os
import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to find <div class="navbar-top">...</div>
    # and <div class="navbar-bottom">...</div>
    # and combine them.

    # Match everything between <nav class="navbar-new"> and </nav>
    nav_pattern = re.compile(r'(<nav class="navbar-new">)(.*?)(</nav>)', re.DOTALL)
    
    def replacer(match):
        inner = match.group(2)
        
        # extract logo
        logo_match = re.search(r'<div class="logo-new">.*?</div>', inner, re.DOTALL)
        # extract nav-links
        links_match = re.search(r'<ul class="nav-links-new">.*?</ul>', inner, re.DOTALL)
        # extract nav-actions
        actions_match = re.search(r'<div class="nav-actions-new">.*?</div>\s*</div>', inner, re.DOTALL) # the last </div> is for navbar-top
        
        if logo_match and links_match and actions_match:
            logo = logo_match.group(0)
            links = links_match.group(0)
            
            # fix actions string to not include the closing div of navbar-top
            actions_full = actions_match.group(0)
            actions = re.sub(r'</div>\s*$', '', actions_full).strip()
            
            new_inner = f'''
        <div class="navbar-desktop-row" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%;">
            {logo}
            {links}
            {actions}
        </div>
'''
            return match.group(1) + new_inner + match.group(3)
        return match.group(0)
        
    new_content = nav_pattern.sub(replacer, content)
    if new_content != content:
        print(f"Updated {file}")
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
