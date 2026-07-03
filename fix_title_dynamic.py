import re

with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

new_logic = '''
            // Filter products
            productCards.forEach(card => {
                if (filterValue === 'all') {
                    card.style.display = 'block';
                } else {
                    if (card.getAttribute('data-category') === filterValue) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                }
            });

            // Update title and subtitle based on filter
            const heroTitle = document.querySelector('.hero-serif-title');
            const heroSub = document.querySelector('.hero-small-text');
            if (heroTitle) {
                if (filterValue === 'all') {
                    heroTitle.textContent = 'COLLECTION';
                    if (heroSub) heroSub.textContent = 'Discover our exquisite jewelry';
                } else if (filterValue === 'her') {
                    heroTitle.textContent = 'Gifts For Her';
                    if (heroSub) heroSub.textContent = 'Curated elegance for the woman you love';
                } else if (filterValue === 'him') {
                    heroTitle.textContent = 'Gifts For Him';
                    if (heroSub) heroSub.textContent = 'Distinguished pieces for him';
                } else {
                    heroTitle.textContent = filterValue.toUpperCase();
                    if (heroSub) heroSub.textContent = 'Explore our ' + filterValue + ' collection';
                }
            }
'''

content = re.sub(
    r'// Filter products\s*productCards.forEach.*?\}\);\s*\}\);', 
    new_logic.strip() + '\n        }', 
    content, 
    flags=re.DOTALL
)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)
