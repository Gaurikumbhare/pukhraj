with open("styles.css", "r", encoding="utf-8") as f:
    content = f.read()

new_css = '''
/* 2-Column Mobile Fixes for Products and Banners */
@media (max-width: 768px) {
    .product-grid-4 {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 1rem !important;
    }
    
    .product-info h3 {
        font-size: 0.8rem;
    }
    
    .product-info .price {
        font-size: 0.85rem;
    }

    .shop-recipient-flex {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 1rem !important;
    }
    
    .shop-recipient-flex .recipient-large-card {
        min-width: 0 !important;
        height: 300px !important;
    }
    
    .recipient-overlay span {
        font-size: 0.9rem !important;
    }
    
    .staggered-grid {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 1rem !important;
    }
    
    .staggered-item {
        min-width: 0 !important;
        height: 300px !important;
        margin-top: 0 !important;
    }
}
'''
content += new_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(content)
