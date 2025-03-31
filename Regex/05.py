# Replace Multiple Spaces with a Single Space in a Sentence

import re

text = "This   is  an    example   sentence."
cleaned_text = re.sub(r'\s+', ' ', text)

print("Cleaned Sentence:", cleaned_text)
