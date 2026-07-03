with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

# The extra lines are "        });\n    }\n});\n" at the very end
import re
content = re.sub(r'\s*\}\);\s*\}\);\s*\}\);\s*$', '\n            });\n        });\n    }\n});\n', content)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)
