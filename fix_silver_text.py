import re

filepath = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj\silver-artifacts.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the badges
content = re.sub(r'<div class="artifact-img-badge">.*?</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="artifact-img-badge-right">.*?</div>', '', content, flags=re.DOTALL)

# Add padding and justification to the CSS
content = content.replace(
    '.artifact-text-wrap {\n                    flex: 1;\n                }',
    '.artifact-text-wrap {\n                    flex: 1;\n                    padding: 0 2rem;\n                }'
)

content = content.replace(
    '.artifact-desc-light {\n                    font-size: 0.95rem;\n                    line-height: 1.8;\n                    color: #666;\n                    margin-bottom: 2.5rem;\n                }',
    '.artifact-desc-light {\n                    font-size: 0.95rem;\n                    line-height: 1.8;\n                    color: #666;\n                    margin-bottom: 2.5rem;\n                    text-align: justify;\n                }'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
