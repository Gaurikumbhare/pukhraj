import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_flex_content = '''<div class="shop-recipient-flex" style="display: flex; gap: 2rem; justify-content: center; max-width: 1200px; margin: 0 auto; flex-wrap: wrap;">
                  <a href="collection.html?filter=her" class="recipient-large-card" style="flex: 1; min-width: 300px; position: relative; height: 500px; overflow: hidden; border-radius: 4px; display: block;">
                      <img src="assets/j5.jpg" alt="Gifts For Her" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;">
                      <div class="recipient-overlay" style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 2rem; background: linear-gradient(transparent, rgba(0,0,0,0.7)); color: #fff; text-align: center;">
                          <span style="font-size: 1.2rem; font-weight: 500; letter-spacing: 1px;">Gifts For Her &rarr;</span>
                      </div>
                  </a>
                  <a href="collection.html?filter=him" class="recipient-large-card" style="flex: 1; min-width: 300px; position: relative; height: 500px; overflow: hidden; border-radius: 4px; display: block;">
                      <img src="assets/j6.jpg" alt="Gifts For Him" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;">
                      <div class="recipient-overlay" style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 2rem; background: linear-gradient(transparent, rgba(0,0,0,0.7)); color: #fff; text-align: center;">
                          <span style="font-size: 1.2rem; font-weight: 500; letter-spacing: 1px;">Gifts For Him &rarr;</span>
                      </div>
                  </a>
              </div>'''

content = re.sub(r'<div class="shop-recipient-flex".*?</div>', new_flex_content, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
