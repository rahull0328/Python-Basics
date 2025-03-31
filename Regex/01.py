# Validate an Email Address

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

email = "example@gmail.com"
print("Valid Email" if is_valid_email(email) else "Invalid Email")
