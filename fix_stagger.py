import re

with open("styles.css", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the staggered-grid rules in the mobile media query
new_staggered = '''
    .staggered-grid {
        display: flex !important;
        flex-wrap: nowrap !important;
        gap: 0.5rem !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .staggered-item {
        min-width: 0 !important;
        flex: 1 !important;
    }
    
    .staggered-item.small {
        height: 180px !important;
    }
    
    .staggered-item.large {
        height: 240px !important;
        margin-top: -20px !important;
        z-index: 2 !important;
    }
    
    .staggered-label {
        font-size: 0.65rem !important;
        bottom: 10px !important;
    }
'''

content = re.sub(r'\s*\.staggered-grid\s*\{.*?\.staggered-item\s*\{.*?\}', new_staggered, content, flags=re.DOTALL)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(content)
