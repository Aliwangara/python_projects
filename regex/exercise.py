# Let’s start with Exercise 1 — Quantifiers & counts (easy) 💪

import re

# Goal:
# Find all 2–4 digit numbers in this string:

count_digit = "Room 12, Bldg 202, apt 34567, code 77"
count_match = re.findall(r"\b\d{2,4}\b", count_digit)
# \b\d{2,4}\b = sets boundary the digits can take
print(count_match)

# Write a regex to find all 5-letter words in this text:

find_letter = "The quick brown fox jumps over the lazy zebra and tiger."


find_match = re.findall(r"\b\w{5}\b", find_letter)
print(find_match)



text = """
Order #12345: 2025-10-22
Order #67890: 2025-11-01
"""

order_match = re.findall(r"#(\d+): (\d{4}-\d{2}-\d{2})", text)
print(order_match)


non_capturing_text = "bat cat fat hat mat rat"
non_capturing_match = re.findall(r"(?:b|c|f|h|m|r)at", non_capturing_text)
print(non_capturing_match)

