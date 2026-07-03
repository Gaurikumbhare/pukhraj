with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('// Product Filter Logic')
if idx != -1:
    content = content[:idx] + '''// Product Filter Logic
document.addEventListener('DOMContentLoaded', function() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const productCards = document.querySelectorAll('.product-grid-4 .product-card');

    if (filterBtns.length > 0 && productCards.length > 0) {
        
        function applyFilter(filterValue) {
            // Update active state of buttons
            filterBtns.forEach(b => {
                if(b.getAttribute('data-filter') === filterValue) {
                    b.classList.add('active');
                } else {
                    b.classList.remove('active');
                }
            });

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
        }

        // Apply URL filter on load if present
        const urlParams = new URLSearchParams(window.location.search);
        const urlFilter = urlParams.get('filter');
        if (urlFilter) {
            applyFilter(urlFilter);
        }

        filterBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const filterValue = this.getAttribute('data-filter');
                
                const path = window.location.pathname;
                if (path.endsWith('/') || path.endsWith('index.html')) {
                    window.location.href = 'collection.html?filter=' + filterValue;
                } else {
                    applyFilter(filterValue);
                    window.history.replaceState(null, '', '?filter=' + filterValue);
                }
            });
        });
    }
});
'''
    with open("script.js", "w", encoding="utf-8") as f:
        f.write(content)
