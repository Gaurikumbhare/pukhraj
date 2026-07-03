import os
import glob
import re

nav_actions = '''            <div class="nav-actions-new">
                <a href="#" class="icon-btn-new mobile-search-icon" title="Search" style="display: none;">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </a>
                <a href="#" class="icon-btn-new cart-icon-new" id="wishlist-icon" title="Wishlist">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    <span class="badge-count" id="wishlist-count" style="position: absolute; top: -4px; right: -6px;">0</span>
                </a>
                <div class="icon-btn-new cart-icon-new" id="cart-icon" title="View Cart">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
                    <span class="cart-count" style="position: absolute; top: -4px; right: -6px;">0</span>
                </div>
                <a href="#" class="icon-btn-new" title="Lightning">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                </a>
            </div>
        </div>
'''

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # check if nav-actions-new is already there
    if 'class="nav-actions-new"' in content:
        continue
    
    # find where to replace
    pattern = re.compile(r'(\s*<div class="logo-new">.*?</div>\s*)<!-- Bottom Row -->', re.DOTALL)
    
    if pattern.search(content):
        print(f"Modifying {file}...")
        new_content = pattern.sub(rf'\1{nav_actions}        <!-- Bottom Row -->', content)
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)

