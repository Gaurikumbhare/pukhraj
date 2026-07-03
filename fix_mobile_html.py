import re
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add close button inside nav-links-new
if '<button class="close-menu-btn">&times;</button>' not in content:
    content = content.replace('<ul class="nav-links-new">', '<ul class="nav-links-new">\n                <button class="close-menu-btn">&times;</button>')

# 2. Add hamburger menu toggle inside navbar-desktop-row, before the logo
menu_toggle_html = '''
            <div class="menu-toggle" id="mobile-menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            </div>'''
if '<div class="menu-toggle"' not in content:
    content = content.replace('<div class="logo-new">', menu_toggle_html + '\n            <div class="logo-new">')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# 3. Add JS for mobile menu toggle
if 'mobileMenuBtn.addEventListener' not in js_content:
    menu_js = '''
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.getElementById('mobile-menu');
    const navLinksNew = document.querySelector('.nav-links-new');
    const closeMenuBtn = document.querySelector('.close-menu-btn');
    
    if (mobileMenuBtn && navLinksNew) {
        mobileMenuBtn.addEventListener('click', function() {
            navLinksNew.classList.add('active');
        });
    }
    if (closeMenuBtn && navLinksNew) {
        closeMenuBtn.addEventListener('click', function() {
            navLinksNew.classList.remove('active');
        });
    }
});
'''
    with open("script.js", "a", encoding="utf-8") as f:
        f.write('\n' + menu_js)
