import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Add inline margin to filter-menu-container
    content = content.replace('<div class="filter-menu-container">', '<div class="filter-menu-container" style="margin-bottom: 3rem !important; margin-top: 1.5rem !important;">')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
