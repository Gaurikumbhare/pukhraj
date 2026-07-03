import re
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'<div class="square-categories">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
# actually let's just do it cleanly

lines = content.split('\n')
start = -1
end = -1
for i, line in enumerate(lines):
    if '<div class="square-categories">' in line:
        start = i
    if start != -1 and '</a>' in line and '</div>' in lines[i+1]:
        end = i + 1
        break

if start != -1 and end != -1:
    del lines[start:end+1]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write('\n'.join(lines))
    print("Removed")
else:
    print("Not found properly")

