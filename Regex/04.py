# Find All URLs in a Given Text

import re

text = "Check out https://example.com and http://test.org for more details."

pattern = r'https?://[^\s]+'
urls = re.findall(pattern, text)

print("URLs Found:", urls)
