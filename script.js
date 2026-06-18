document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');

    if(mobileMenu) {
        mobileMenu.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Inject Cart and Modal HTML
    const injectHTML = `
    <!-- Cart -->
    <div class="cart-sidebar" id="cart-sidebar">
        <div class="cart-header">
            <h2>Your Cart</h2>
            <button id="close-cart" class="close-cart">&times;</button>
        </div>
        <div class="cart-items" id="cart-items">
            <p style="padding: 1rem; color: #777;">Your cart is empty.</p>
        </div>
        <div class="cart-footer">
            <h3>Total: ₹<span id="cart-total">0</span></h3>
            <button class="btn checkout-btn" onclick="window.location.href='checkout.html'" style="width: 100%; margin-top: 1rem;">Checkout</button>
        </div>
    </div>
    <div class="cart-overlay" id="cart-overlay"></div>

    <!-- Product Modal -->
    <div class="product-modal-overlay" id="product-modal-overlay"></div>
    <div class="product-modal" id="product-modal">
        <button class="close-modal" id="close-modal">&times;</button>
        <div class="product-modal-content">
            <div class="product-modal-image" id="modal-image"></div>
            <div class="product-modal-details">
                <p class="modal-subtitle" style="color: var(--primary-color); font-weight: 600; font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 0.5rem; text-transform: uppercase;">Premium Jewelry</p>
                <h2 id="modal-title">Product Name</h2>
                <div class="modal-reviews" style="color: #f5b301; margin-bottom: 1rem; font-size: 0.9rem;">
                    ★★★★★ <span style="color: #777; margin-left: 5px;">(125 customer reviews)</span>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <span class="modal-price" id="modal-price" style="color: var(--primary-color); font-size: 2rem; font-weight: 600;">₹0</span>
                    <span style="display: block; font-size: 0.8rem; color: #888; margin-top: 5px; font-style: italic;">* Price may vary based on daily market rates.</span>
                </div>
                
                <p class="modal-desc" id="modal-desc">Product description goes here.</p>
                
                <hr style="border: none; border-top: 1px solid #eee; margin: 1.5rem 0;">

                <div class="product-specs">
                    <div class="spec-row">
                        <strong>Item ID:</strong> <span id="modal-item-id">#JW-000</span>
                    </div>
                    <div class="spec-row">
                        <strong>Metal:</strong> <span id="modal-metal">22K Gold</span>
                    </div>
                    
                    <div class="spec-group" style="margin-top: 1.5rem;">
                        <label style="display: block; font-weight: bold; margin-bottom: 0.8rem; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;">Select Weight</label>
                        <div class="weight-pills" style="display: flex; gap: 10px;">
                            <span class="weight-pill active" id="modal-weight" style="padding: 0.5rem 1.5rem; border: 1px solid var(--primary-color); border-radius: 30px; color: var(--primary-color); cursor: pointer;">15 gm</span>
                        </div>
                    </div>
                </div>

                <div style="display: flex; gap: 1rem; margin-top: 2.5rem;">
                    <button class="btn" id="modal-add-to-cart" style="flex: 1; padding: 1rem;">Add to Cart</button>
                    <button class="btn checkout-btn-direct" onclick="window.location.href='checkout.html'" style="flex: 1; background: var(--text-color); color: #fff; padding: 1rem;">Buy Now</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Search Modal -->
    <div class="search-modal" id="search-modal">
        <button class="close-modal" id="close-search" style="top: 20px; right: 30px; font-size: 3rem;">&times;</button>
        <div class="search-container">
            <input type="text" id="search-input" placeholder="Search jewelry (e.g. Necklace, Rings)...">
            <div id="search-results" class="search-results"></div>
        </div>
    </div>

    <!-- Login Modal -->
    <div class="login-modal-overlay" id="login-modal-overlay"></div>
    <div class="login-modal" id="login-modal">
        <button class="close-modal" id="close-login">&times;</button>
        <h2 style="color: var(--primary-color); margin-bottom: 1.5rem; text-align: center; font-family: var(--font-heading);">Welcome Back</h2>
        <form id="login-form">
            <div style="margin-bottom: 1rem;">
                <label style="display: block; margin-bottom: 0.5rem; color: #555; font-weight: 500;">Email</label>
                <input type="email" required style="width: 100%; padding: 0.8rem 1rem; border: 1px solid #ddd; border-radius: 4px; font-family: var(--font-body); outline: none;">
            </div>
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; color: #555; font-weight: 500;">Password</label>
                <input type="password" required style="width: 100%; padding: 0.8rem 1rem; border: 1px solid #ddd; border-radius: 4px; font-family: var(--font-body); outline: none;">
            </div>
            <button type="submit" class="btn" style="width: 100%; padding: 1rem;">Sign In</button>
            <p style="text-align: center; margin-top: 1.5rem; color: #777; font-size: 0.9rem;">Don't have an account? <a href="#" style="color: var(--primary-color); font-weight: 600; text-decoration: none;">Sign up</a></p>
        </form>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', injectHTML);

    // Cart Logic
    let cart = JSON.parse(localStorage.getItem('pukhraj_cart')) || [];
    
    const cartIcon = document.getElementById('cart-icon');
    const cartSidebar = document.getElementById('cart-sidebar');
    const closeCart = document.getElementById('close-cart');
    const cartOverlay = document.getElementById('cart-overlay');
    const cartCountElements = document.querySelectorAll('.cart-count');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');

    function updateCartUI() {
        // Update count
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        cartCountElements.forEach(el => el.textContent = totalItems);

        // Update items list
        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p style="padding: 1rem; color: #777;">Your cart is empty.</p>';
            cartTotalElement.textContent = '0';
        } else {
            cartItemsContainer.innerHTML = cart.map(item => `
                <div class="cart-item">
                    <div>
                        <h4>${item.name}</h4>
                        <p>₹${item.price.toLocaleString('en-IN')} x ${item.quantity}</p>
                    </div>
                    <button class="remove-item" data-id="${item.id}">&times;</button>
                </div>
            `).join('');

            // Update total
            const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
            cartTotalElement.textContent = total.toLocaleString('en-IN');

            // Attach remove events
            document.querySelectorAll('.remove-item').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const id = e.target.getAttribute('data-id');
                    removeFromCart(id);
                });
            });
        }
        localStorage.setItem('pukhraj_cart', JSON.stringify(cart));
    }

    function addToCart(id, name, price) {
        const existingItem = cart.find(item => item.id === id);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ id, name, price: parseInt(price), quantity: 1 });
        }
        updateCartUI();
        cartSidebar.classList.add('open');
        cartOverlay.classList.add('open');
    }

    function removeFromCart(id) {
        cart = cart.filter(item => item.id !== id);
        updateCartUI();
    }

    // Toggle Cart
    if(cartIcon) {
        cartIcon.addEventListener('click', () => {
            cartSidebar.classList.add('open');
            cartOverlay.classList.add('open');
        });
    }

    if(closeCart) {
        closeCart.addEventListener('click', () => {
            cartSidebar.classList.remove('open');
            cartOverlay.classList.remove('open');
        });
    }

    if(cartOverlay) {
        cartOverlay.addEventListener('click', () => {
            cartSidebar.classList.remove('open');
            cartOverlay.classList.remove('open');
        });
    }

    // Add to Cart Buttons
    document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent opening modal when clicking add to cart
            const card = e.target.closest('.card');
            const name = card.querySelector('h3').textContent;
            const priceText = card.querySelector('p').textContent;
            const price = priceText.replace(/[^0-9]/g, '');
            // Generate a simple ID based on name
            const id = name.toLowerCase().replace(/[^a-z0-9]/g, '-');
            addToCart(id, name, price);
        });
    });

    // Product Modal Logic
    const modal = document.getElementById('product-modal');
    const modalOverlay = document.getElementById('product-modal-overlay');
    const closeModal = document.getElementById('close-modal');
    const modalImg = document.getElementById('modal-image');
    const modalTitle = document.getElementById('modal-title');
    const modalPrice = document.getElementById('modal-price');
    const modalDesc = document.getElementById('modal-desc');
    const modalAddToCartBtn = document.getElementById('modal-add-to-cart');

    const modalItemId = document.getElementById('modal-item-id');
    const modalMetal = document.getElementById('modal-metal');
    const modalWeight = document.getElementById('modal-weight');

    function openModal(card) {
        const title = card.querySelector('h3').textContent;
        const price = card.querySelector('p').textContent;
        const bgImg = card.querySelector('.card-img').style.backgroundImage;
        
        const desc = card.getAttribute('data-description') || "Indulge in our artisanal jewelry piece. Handcrafted with the finest materials and a perfect balance of elegance and tradition.";
        const itemId = card.getAttribute('data-id') || "#JW-" + Math.floor(Math.random() * 900 + 100);
        const metal = card.getAttribute('data-metal') || "22K Gold";
        const weight = card.getAttribute('data-weight') || "10 gm";
        
        modalTitle.textContent = title;
        modalPrice.textContent = price;
        modalDesc.textContent = desc;
        modalImg.style.backgroundImage = bgImg;
        
        modalItemId.textContent = itemId;
        modalMetal.textContent = metal;
        modalWeight.textContent = weight;
        
        // Setup Add to Cart inside modal
        modalAddToCartBtn.onclick = () => {
            const rawPrice = price.replace(/[^0-9]/g, '');
            const id = title.toLowerCase().replace(/[^a-z0-9]/g, '-');
            addToCart(id, title, rawPrice);
            
            // Give user feedback
            modalAddToCartBtn.textContent = "Added to Cart ✓";
            modalAddToCartBtn.style.backgroundColor = "green";
            modalAddToCartBtn.style.color = "white";
            
            setTimeout(() => {
                modalAddToCartBtn.textContent = "Add to Cart";
                modalAddToCartBtn.style.backgroundColor = "";
                modalAddToCartBtn.style.color = "";
            }, 2000);
        };

        modalOverlay.classList.add('show');
        modal.classList.add('show');
        
        // Small delay for transition
        setTimeout(() => {
            modalOverlay.classList.add('open');
            modal.classList.add('open');
        }, 10);
    }

    function closeModalFunc() {
        modalOverlay.classList.remove('open');
        modal.classList.remove('open');
        setTimeout(() => {
            modalOverlay.classList.remove('show');
            modal.classList.remove('show');
        }, 300);
    }

    if(closeModal) closeModal.addEventListener('click', closeModalFunc);
    if(modalOverlay) modalOverlay.addEventListener('click', closeModalFunc);

    // Open modal when clicking on card image or title
    document.querySelectorAll('.card-img, .card h3').forEach(el => {
        el.style.cursor = 'pointer';
        el.addEventListener('click', (e) => {
            const card = e.target.closest('.card');
            openModal(card);
        });
    });

    // Initialize UI
    updateCartUI();

    // Hero Slider Logic
    const slides = document.querySelectorAll('.slide');
    if(slides.length > 0) {
        const nextBtn = document.querySelector('.next-btn');
        const prevBtn = document.querySelector('.prev-btn');
        const dots = document.querySelectorAll('.dot');
        const slideTrack = document.getElementById('slide-track');
        let currentSlide = 0;
        let slideInterval;

        function goToSlide(n) {
            slides[currentSlide].classList.remove('active');
            dots[currentSlide].classList.remove('active');
            currentSlide = (n + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
            dots[currentSlide].classList.add('active');
            if (slideTrack) {
                slideTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
            }
        }

        function nextSlide() {
            goToSlide(currentSlide + 1);
        }

        function prevSlide() {
            goToSlide(currentSlide - 1);
        }

        function startSlideShow() {
            slideInterval = setInterval(nextSlide, 5000); // 5 seconds
        }

        function stopSlideShow() {
            clearInterval(slideInterval);
        }

        if(nextBtn) {
            nextBtn.addEventListener('click', () => {
                nextSlide();
                stopSlideShow();
                startSlideShow();
            });
        }

        if(prevBtn) {
            prevBtn.addEventListener('click', () => {
                prevSlide();
                stopSlideShow();
                startSlideShow();
            });
        }

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                goToSlide(index);
                stopSlideShow();
                startSlideShow();
            });
        });

        startSlideShow();
    }

    // Collection Filter Logic
    const filterBtns = document.querySelectorAll('.filter-btn');
    const megaFilters = document.querySelectorAll('.mega-filter');
    const collectionCards = document.querySelectorAll('#collection .card');
    
    let currentCategory = 'all';
    let currentPrice = 'all';
    let currentGender = 'all';

    if (collectionCards.length > 0) {
        
        function applyFilters() {
            collectionCards.forEach(card => {
                let match = true;
                
                // Check Category / Metal Implicitly
                // The main buttons actually represent different things. 'all', 'gold', 'silver', 'rings', 'necklace', 'bangles'
                if (currentCategory !== 'all') {
                    const categories = card.getAttribute('data-category') || '';
                    if (!categories.includes(currentCategory)) match = false;
                }
                
                // Check Gender
                if (currentGender !== 'all') {
                    const cardGender = card.getAttribute('data-gender') || 'all';
                    if (cardGender !== 'all' && cardGender !== currentGender) match = false;
                }
                
                // Check Price
                if (currentPrice !== 'all') {
                    const price = parseInt(card.getAttribute('data-price') || '0');
                    if (currentPrice === 'under20' && price >= 20000) match = false;
                    else if (currentPrice === '20to50' && (price < 20000 || price > 50000)) match = false;
                    else if (currentPrice === '50to100' && (price < 50000 || price > 100000)) match = false;
                    else if (currentPrice === 'over100' && price <= 100000) match = false;
                }
                
                card.style.display = match ? 'block' : 'none';
            });
        }

        // Attach Event Listeners to Top Icons (Main Categories)
        if (filterBtns.length > 0) {
            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Reset sub-filters when main category changes
                    currentPrice = 'all';
                    currentGender = 'all';
                    currentCategory = btn.getAttribute('data-filter');
                    
                    filterBtns.forEach(b => {
                        b.classList.remove('active');
                        b.style.color = '#666'; 
                    });
                    btn.classList.add('active');
                    btn.style.color = 'var(--primary-color)';
                    
                    // Reset styling on mega menu links
                    megaFilters.forEach(m => m.style.fontWeight = 'normal');
                    
                    applyFilters();
                });
            });
        }
        
        // Attach Event Listeners to Mega Menu Links
        if (megaFilters.length > 0) {
            megaFilters.forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Auto-select the parent category icon
                    const parentItem = link.closest('.filter-item');
                    if (parentItem) {
                        const parentBtn = parentItem.querySelector('.filter-btn');
                        if (parentBtn && !parentBtn.classList.contains('active')) {
                            parentBtn.click(); // This will reset currentPrice/Gender and set category
                        }
                    }
                    
                    const type = link.getAttribute('data-type');
                    const val = link.getAttribute('data-value');
                    
                    if (type === 'price') currentPrice = val;
                    if (type === 'gender') currentGender = val;
                    
                    // Update bold styling to show active state in mega menu
                    parentItem.querySelectorAll(`[data-type="${type}"]`).forEach(m => m.style.fontWeight = 'normal');
                    link.style.fontWeight = 'bold';
                    link.style.color = 'var(--primary-color)';
                    
                    applyFilters();
                });
            });
        }
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
                navLinks.classList.remove('active');
            }
        });
    });
    // --- Search & Profile Icon Logic ---
    const searchBtn = document.querySelector('a[title="Search"]');
    const profileBtn = document.querySelector('a[title="Profile"]');
    
    const searchModalDOM = document.getElementById('search-modal');
    const closeSearch = document.getElementById('close-search');
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    const loginModalDOM = document.getElementById('login-modal');
    const loginOverlay = document.getElementById('login-modal-overlay');
    const closeLogin = document.getElementById('close-login');
    const loginForm = document.getElementById('login-form');

    // Build catalog for search
    let productCatalog = [];
    document.querySelectorAll('.card').forEach(card => {
        const bgImgStyle = card.querySelector('.card-img').style.backgroundImage;
        if(bgImgStyle) {
            const imgSrc = bgImgStyle.replace(/^url\(["']?/, '').replace(/["']?\)$/, '');
            const titleEl = card.querySelector('h3');
            const priceEl = card.querySelector('p');
            if(titleEl && priceEl) {
                productCatalog.push({
                    title: titleEl.textContent,
                    price: priceEl.textContent,
                    img: imgSrc,
                    element: card
                });
            }
        }
    });

    if (searchBtn && searchModalDOM) {
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            searchModalDOM.classList.add('show');
            setTimeout(() => {
                searchModalDOM.classList.add('open');
                searchInput.focus();
            }, 10);
        });
    }

    if (closeSearch && searchModalDOM) {
        closeSearch.addEventListener('click', () => {
            searchModalDOM.classList.remove('open');
            setTimeout(() => searchModalDOM.classList.remove('show'), 300);
        });
    }

    if (searchInput && searchResults) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            searchResults.innerHTML = '';
            if (query.length === 0) return;

            const results = productCatalog.filter(p => p.title.toLowerCase().includes(query));
            if (results.length === 0) {
                searchResults.innerHTML = '<p style="color: #777;">No matching jewelry found.</p>';
                return;
            }

            results.forEach(res => {
                const item = document.createElement('div');
                item.className = 'search-item';
                item.innerHTML = `
                    <img src="${res.img}" alt="${res.title}">
                    <div class="search-item-info">
                        <h4>${res.title}</h4>
                        <p>${res.price}</p>
                    </div>
                `;
                item.addEventListener('click', () => {
                    searchModalDOM.classList.remove('open');
                    setTimeout(() => searchModalDOM.classList.remove('show'), 300);
                    openModal(res.element); // open quick view modal
                });
                searchResults.appendChild(item);
            });
        });
    }

    // Login Logic
    if (profileBtn && loginOverlay) {
        profileBtn.addEventListener('click', (e) => {
            e.preventDefault();
            loginOverlay.classList.add('show');
            loginModalDOM.classList.add('show');
            setTimeout(() => {
                loginOverlay.classList.add('open');
                loginModalDOM.classList.add('open');
            }, 10);
        });
    }

    function closeLoginFunc() {
        if(loginOverlay) loginOverlay.classList.remove('open');
        if(loginModalDOM) loginModalDOM.classList.remove('open');
        setTimeout(() => {
            if(loginOverlay) loginOverlay.classList.remove('show');
            if(loginModalDOM) loginModalDOM.classList.remove('show');
        }, 300);
    }

    if (closeLogin) closeLogin.addEventListener('click', closeLoginFunc);
    if (loginOverlay) loginOverlay.addEventListener('click', closeLoginFunc);
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Welcome! You have successfully logged in.');
            closeLoginFunc();
        });
    }
});
