with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

inline_css = '''
<style>
@media (min-width: 769px) {
    .close-menu-btn {
        display: none !important;
    }
}
</style>
'''

content = content.replace('</head>', inline_css + '\n</head>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
