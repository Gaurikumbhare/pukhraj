with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

inline_css = '''
<style>
.add-to-bag-btn {
    position: absolute !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 100% !important;
    background: var(--primary-color, #1a3641) !important;
    color: #fff !important;
    border: none !important;
    padding: 12px 0 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    opacity: 0 !important; 
    transform: translateY(10px) !important;
    z-index: 10 !important;
}

.product-img-wrapper {
    position: relative !important;
    overflow: hidden !important;
}

.product-img-wrapper:hover .add-to-bag-btn {
    opacity: 1 !important;
    transform: translateY(0) !important;
}

.add-to-bag-btn:hover {
    background: #0d1b21 !important;
}
</style>
'''

content = content.replace('</head>', inline_css + '\n</head>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
