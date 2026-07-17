import re

with open('collection.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the badge
new_content = re.sub(r'\s*<span class="badge best-seller">Best Seller</span>', '', content)

if new_content != content:
    with open('collection.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Removed Best Seller badges from collection.html')
else:
    print('No changes made.')
