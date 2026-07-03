import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Bump cache buster for styles
    content = content.replace('styles.css?v=11', 'styles.css?v=12')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
