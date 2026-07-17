import glob
import re

new_search_html = '''    <div class="login-modal-overlay" id="search-modal-overlay"></div>
    <div class="search-modal" id="search-modal" style="width: 90%; max-width: 350px; padding: 0.2rem 0.5rem; background: #fff; border-radius: 30px; display: flex; align-items: center; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
        <div class="search-container" style="display: flex; align-items: center; width: 100%;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2" style="margin-left: 0.8rem;">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input type="text" id="mobile-search-input" placeholder="Search..." style="flex: 1; border: none; outline: none; padding: 0.8rem 1rem; font-size: 1rem; background: transparent; color: #333; font-family: var(--font-body);">
            <button id="close-search-modal" style="background: none; border: none; cursor: pointer; padding: 0.5rem; color: #666; transition: color 0.3s; display: flex; align-items: center; justify-content: center;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
        </div>
    </div>'''

updated = 0
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the current search modal block
    pattern = r'<div class="login-modal-overlay" id="search-modal-overlay"></div>\s*<div class="search-modal" id="search-modal".*?</button>\s*</div>\s*</div>'
    
    new_content = re.sub(pattern, new_search_html, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1

print(f'Updated search HTML to compact version in {updated} files')
