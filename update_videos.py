import re

filepath = r'c:\Users\gauri\OneDrive\Desktop\Pukhraj\about.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the 2nd, 3rd, and 4th occurrence of:
# <video src="assets/WhatsApp%20Video%202026-07-16%20at%204.41.39%20PM.mp4" autoplay muted loop playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>

# Count occurrences just to be sure
count = content.count('WhatsApp%20Video%202026-07-16%20at%204.41.39%20PM.mp4')
print(f"Found {count} instances.")

# Split by the video string
parts = content.split('WhatsApp%20Video%202026-07-16%20at%204.41.39%20PM.mp4')

if len(parts) == 5:
    # Reconstruct the string
    new_content = parts[0] + 'WhatsApp%20Video%202026-07-16%20at%204.41.39%20PM.mp4' + \
                  parts[1] + 'video%202.mp4' + \
                  parts[2] + 'video%203.mp4' + \
                  parts[3] + 'video%204.mp4' + \
                  parts[4]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully.")
else:
    print("Error: Expected 4 instances of the video, found something else.")
