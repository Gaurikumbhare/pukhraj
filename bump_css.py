import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Add cache buster to styles.css
    content = content.replace('styles.css?v=7', 'styles.css?v=8')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
