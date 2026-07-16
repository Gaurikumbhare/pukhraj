import os
import glob

files = glob.glob(r'c:\Users\gauri\OneDrive\Desktop\Pukhraj\*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'margin-bottom: 3rem;' in content and 'hero-static' in content:
        # replace the specific margin on the hero static inline style
        content = content.replace('margin-bottom: 3rem;"', 'margin-bottom: 0;"')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {os.path.basename(file)}')

print('Done')
