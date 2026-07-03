import re

with open("styles.css", "r", encoding="utf-8") as f:
    content = f.read()

# Remove old add-to-bag-btn styles completely
content = re.sub(r'\.add-to-bag-btn\s*\{.*?\}(?=\s*\.add-to-bag-btn:hover|\s*\.)', '', content, flags=re.DOTALL)
content = re.sub(r'\.add-to-bag-btn:hover\s*\{.*?\}(?=\s*\.)', '', content, flags=re.DOTALL)

# Add new premium add-to-bag-btn styles
new_css = '''
.add-to-bag-btn {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    background: var(--primary-color);
    color: #fff;
    border: none;
    padding: 14px 0;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.3s ease;
    opacity: 0; 
    transform: translateY(100%);
    z-index: 3;
    font-family: var(--font-body);
}

.product-img-wrapper {
    position: relative;
    overflow: hidden;
}

.product-img-wrapper:hover .add-to-bag-btn {
    opacity: 1;
    transform: translateY(0);
}

.add-to-bag-btn:hover {
    background: #172d36;
}

@media (max-width: 768px) {
    .add-to-bag-btn {
        opacity: 1;
        transform: translateY(0);
        position: relative;
        margin-top: 10px;
        border-radius: 4px;
        padding: 10px 0;
    }
}
'''

content += new_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(content)
