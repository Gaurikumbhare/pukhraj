import os

filepath = r"c:\Users\gauri\OneDrive\Desktop\jweller\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

old_her = """<a href="new-arrivals.html" class="recipient-large-card" style="flex: 1; min-width: 300px; position: relative; height: 500px; overflow: hidden; border-radius: 4px; display: block;">
                    <img src="assets/j5.jpg" alt="Gifts For Her\""""
new_her = """<a href="collection.html?filter=her" class="recipient-large-card" style="flex: 1; min-width: 300px; position: relative; height: 500px; overflow: hidden; border-radius: 4px; display: block;">
                    <img src="assets/j5.jpg" alt="Gifts For Her\""""
content = content.replace(old_her, new_her)

old_him = """<a href="new-arrivals.html" class="recipient-large-card" style="flex: 1; min-width: 300px; position: relative; height: 500px; overflow: hidden; border-radius: 4px; display: block;">
                    <img src="assets/j6.jpg" alt="Gifts For Him\""""
new_him = """<a href="collection.html?filter=him" class="recipient-large-card" style="flex: 1; min-width: 300px; position: relative; height: 500px; overflow: hidden; border-radius: 4px; display: block;">
                    <img src="assets/j6.jpg" alt="Gifts For Him\""""
content = content.replace(old_him, new_him)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated links successfully.")
