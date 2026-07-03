import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Add cache buster to script.js
    content = content.replace('script.js?v=3', 'script.js?v=4')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
