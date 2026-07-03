import re

with open("styles.css", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the absolute positioning of sku-header to make it relative
content = re.sub(
    r'\.sku-header\s*\{\s*position:\s*absolute;\s*top:\s*40px;\s*left:\s*50%;\s*transform:\s*translateX\(-50%\);',
    '.sku-header { position: relative; text-align: left; margin-bottom: 1rem;',
    content
)

# Add a safety catch for mobile just in case
new_css = '''
/* Product Page Fixes */
@media (max-width: 768px) {
    .sku-header {
        position: relative !important;
        top: 0 !important;
        left: 0 !important;
        transform: none !important;
        text-align: left !important;
        padding: 0 0 1rem 0 !important;
        margin-bottom: 1rem !important;
        border: none !important;
        width: 100% !important;
    }
}
'''
content += new_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(content)
