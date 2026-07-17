import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add class to the left button
content = content.replace('style="position: absolute; left: 0; z-index: 10;', 'class="testimonial-arrow" style="position: absolute; left: -15px; z-index: 10;')

# Add class to the right button
content = content.replace('style="position: absolute; right: 0; z-index: 10;', 'class="testimonial-arrow" style="position: absolute; right: -15px; z-index: 10;')

# Add CSS to hide on mobile
css = '''
<style>
@media (max-width: 768px) {
    .testimonial-arrow {
        display: none !important;
    }
}
</style>
'''
if '.testimonial-arrow' not in content:
    content = content.replace('</head>', css + '</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html to hide testimonial arrows on mobile and adjust desktop position')
