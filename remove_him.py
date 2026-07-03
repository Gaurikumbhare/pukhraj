import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the 'Gifts For Him' block from Shop For Someone
content = re.sub(
    r'<a href="collection\.html\?filter=him".*?</a>',
    '',
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
