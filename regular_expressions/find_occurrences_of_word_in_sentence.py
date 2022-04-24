import re

text = input()
word = input()

expression = rf"\b{word}\b"

matches = re.findall(expression, text, flags=re.IGNORECASE)

print(len(matches))