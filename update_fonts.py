import os
import re

css_path = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("--font-heading: 'Inter', sans-serif;", "--font-heading: 'Playfair Display', serif;")
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update HTML files
html_dir = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj'
new_font_link = 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Nunito+Sans:wght@300;400;600&family=Inter:wght@300;400;500&display=swap'

# Replace any occurrence of the old font URLs (which might not have Playfair Display)
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(html_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find the fonts link and replace its href
        # The href looks like: href="https://fonts.googleapis.com/css2?family=...&display=swap"
        content = re.sub(r'https://fonts\.googleapis\.com/css2\?family=[^"]+display=swap', new_font_link, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated fonts successfully.")
