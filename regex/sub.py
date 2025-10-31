# Use re.sub() to normalize phone numbers into digits-only format.
# Input text:

import re

text = "Call 0712-345-678 or 011-2345678 for help."

text_match = re.sub(r"(\d[\d-]+)", lambda x: re.sub(r"\D", "", x.group()), text)
print(text_match)