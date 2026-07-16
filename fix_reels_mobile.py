import re

filepath = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj\about.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Container:
old_container = 'style="display: flex; gap: 1.5rem; justify-content: center; max-width: 1400px; margin: 0 auto; flex-wrap: wrap;"'
new_container = 'class="reels-grid"'
content = content.replace(old_container, new_container)

# Items:
old_item = 'style="flex: 1 1 0px; min-width: 250px; max-width: 300px; position: relative; height: 500px; border-radius: 12px; overflow: hidden; display: block; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s ease;"'
new_item = 'class="reel-card"'
content = content.replace(old_item, new_item)

old_item2 = 'style="flex: 1; min-width: 250px; max-width: 300px; position: relative; height: 500px; border-radius: 12px; overflow: hidden; display: block; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s ease;"'
content = content.replace(old_item2, new_item)

old_item3 = 'style="flex: 1; min-width: 250px; max-width: 300px; position: relative; aspect-ratio: 9/16; border-radius: 12px; overflow: hidden; display: block; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s ease;"'
content = content.replace(old_item3, new_item)

# Add CSS block
css = '''
    <style>
    .reels-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    .reel-card {
        position: relative;
        height: 500px;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
    }
    .reel-card:hover {
        transform: translateY(-10px);
    }
    @media (max-width: 992px) {
        .reels-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    @media (max-width: 576px) {
        .reels-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
        .reel-card {
            height: 350px; /* Shorter on mobile so they fit nicely */
        }
    }
    </style>
'''
if '<style>\n    .reels-grid' not in content:
    content = content.replace('</head>', css + '</head>')

# Remove filter sidebar from about.html
content = re.sub(r'<!-- Filter Sidebar -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated about.html for mobile responsiveness')
