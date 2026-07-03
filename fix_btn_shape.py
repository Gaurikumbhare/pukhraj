with open("styles.css", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("border-radius: 20px !important;", "border-radius: 2px !important;")
content = content.replace("padding: 6px 18px !important;", "padding: 10px 24px !important;")
content = content.replace("font-size: 0.8rem !important;", "font-size: 0.85rem !important;")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(content)
