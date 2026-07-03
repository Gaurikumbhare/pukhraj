with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

old_logic = "heroTitle.textContent = filterType === 'her' ? 'Gifts For Her' : 'Gifts For Him';"
old_logic_sub = "if (heroSub) heroSub.textContent = filterType === 'her' ? 'Curated elegance for the woman you love' : 'Distinguished pieces for him';"

new_logic = '''if (filterType === 'her') {
                heroTitle.textContent = 'Gifts For Her';
                if (heroSub) heroSub.textContent = 'Curated elegance for the woman you love';
            } else if (filterType === 'him') {
                heroTitle.textContent = 'Gifts For Him';
                if (heroSub) heroSub.textContent = 'Distinguished pieces for him';
            } else {
                heroTitle.textContent = filterType.toUpperCase();
                if (heroSub) heroSub.textContent = 'Explore our ' + filterType + ' collection';
            }'''

content = content.replace(old_logic + "\n            " + old_logic_sub, new_logic)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)
