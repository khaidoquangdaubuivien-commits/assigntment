import re

def hide_phone_numbers(text):
    pattern = r'(\+84\d+|\b\d{10}\b)'
    return re.sub(pattern, "[REDACTED]", text)


doc = "Call me at 0912345678 or +84987654321 tomorrow."
print(hide_phone_numbers(doc))