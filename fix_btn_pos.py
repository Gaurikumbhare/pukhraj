import re
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the inline style I added earlier
new_inline = '''<style>
.add-to-bag-btn {
    width: 100% !important;
    background: #fff !important;
    color: var(--primary-color, #1a3641) !important;
    border: 1px solid var(--primary-color, #1a3641) !important;
    padding: 10px 0 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    margin-top: 10px !important;
    border-radius: 2px !important;
}

.add-to-bag-btn:hover {
    background: var(--primary-color, #1a3641) !important;
    color: #fff !important;
}

.product-img-wrapper {
    position: relative !important;
}
</style>'''

content = re.sub(r'<style>.*?\.add-to-bag-btn.*?</style>', new_inline, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
