with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("path.endswith", "path.endsWith")

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)
