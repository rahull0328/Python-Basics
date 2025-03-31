# Extract All Phone Numbers from a Text

import re

text = "Contact us at +1-800-123-4567 or (123) 456-7890."

pattern = r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
matches = re.findall(pattern, text)

print("Phone Numbers Found:", matches)
