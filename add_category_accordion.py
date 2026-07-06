import os

html_block = """
                <li class="nav-accordion-item">
                    <div class="nav-accordion-header" onclick="this.parentElement.classList.toggle('active')">
                        Shop by Category
                        <span class="nav-accordion-icon"></span>
                    </div>
                    <div class="nav-accordion-content">
                        <div class="category-grid">
                            <a href="necklaces.html" class="category-card">
                                <span>Necklaces & Chains</span>
                                <img src="assets/indian_gold_necklace.png" alt="Necklaces">
                            </a>
                            <a href="bracelets.html" class="category-card">
                                <span>Bracelets</span>
                                <img src="assets/indian_gold_bangles.png" alt="Bracelets">
                            </a>
                            <a href="earrings.html" class="category-card">
                                <span>Earrings</span>
                                <img src="assets/gold_earrings.png" alt="Earrings">
                            </a>
                            <a href="rings.html" class="category-card">
                                <span>Rings</span>
                                <img src="assets/gold_rings.png" alt="Rings">
                            </a>
                            <a href="collection.html" class="category-card">
                                <span>Men's Chains</span>
                                <img src="assets/925_sterling_silver_mens_italy_chain_bracelet_vy_jewelry_178f89b5-4d23-422d-b77a-5703fae9439a_580x@2x.webp" alt="Mens">
                            </a>
                            <a href="collection.html" class="category-card">
                                <span>Jewellery Sets</span>
                                <img src="assets/wedding.png" alt="Sets">
                            </a>
                            <a href="collection.html" class="category-card">
                                <span>Anklets</span>
                                <img src="assets/indian_silver_anklets.png" alt="Anklets">
                            </a>
                            <a href="collection.html" class="category-card">
                                <span>Mangalsutras</span>
                                <img src="assets/station_mangalsutra.png" alt="Mangalsutras">
                            </a>
                        </div>
                        <div style="text-align: center; padding: 1rem 0;">
                            <a href="collection.html" style="text-decoration: underline; font-size: 0.9rem; color: #333;">View all</a>
                        </div>
                    </div>
                </li>"""

directory = r"c:\Users\gauri\OneDrive\Desktop\jweller"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        target = '<button class="close-menu-btn">&times;</button>'
        
        # Check if already added
        if 'Shop by Category' not in content and target in content:
            content = content.replace(target, target + html_block)
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
