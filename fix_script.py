import os
import re

filepath = r"c:\Users\gauri\OneDrive\Desktop\jweller\script.js"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# I will find the last occurrence of the DOMContentLoaded block I added and keep it, or just remove ALL URL Filter Logic and add ONE at the very end.

# Remove anything between `// URL Filter Logic` and `// Initialize UI` (if it was inserted there)
content = re.sub(r'// URL Filter Logic.*?// Initialize UI', '// Initialize UI', content, flags=re.DOTALL)

# Remove the appended block at the bottom
content = re.sub(r"document\.addEventListener\('DOMContentLoaded', \(\) => {\s*// URL Filter Logic.*?}\);\s*", "", content, flags=re.DOTALL)

# Now, append exactly ONE working block at the bottom
filter_logic = """
document.addEventListener('DOMContentLoaded', () => {
    // URL Filter Logic
    const urlParams = new URLSearchParams(window.location.search);
    const filterType = urlParams.get('filter');
    if (filterType) {
        const allCards = document.querySelectorAll('.product-card');
        allCards.forEach(card => {
            const gender = card.getAttribute('data-gender');
            if (gender === filterType || !gender) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
        
        const heroTitle = document.querySelector('.hero-serif-title');
        const heroSub = document.querySelector('.hero-small-text');
        if (heroTitle) {
            heroTitle.textContent = filterType === 'her' ? 'Gifts For Her' : 'Gifts For Him';
        }
        if (heroSub) {
            heroSub.textContent = filterType === 'her' ? 'Curated elegance for the woman you love' : 'Distinguished pieces for him';
        }
    }
});
"""

content += filter_logic

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed script.js syntax errors.")
