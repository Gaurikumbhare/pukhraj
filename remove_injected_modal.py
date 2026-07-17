with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Remove the injected search modal HTML
pattern = r'<!-- Search Modal -->.*?<div class="search-modal" id="search-modal">.*?</div>\s*</div>\s*</div>'
content = re.sub(pattern, '', content, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Removed injected search modal from script.js')
