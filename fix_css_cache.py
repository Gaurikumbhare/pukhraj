import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Bump CSS cache buster
    content = content.replace('styles.css?v=3', 'styles.css?v=4')
    
    # Also inject a style block directly in the head to force aspect-ratio
    if '</style>' in content:
        content = content.replace('</style>', '\n.product-card .product-img-wrapper { height: auto !important; aspect-ratio: 1/1 !important; }\n</style>')
    else:
        content = content.replace('</head>', '<style>\n.product-card .product-img-wrapper { height: auto !important; aspect-ratio: 1/1 !important; }\n</style>\n</head>')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
