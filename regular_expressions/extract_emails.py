import re

text = input()

email_expression = re.compile(r'(^|(?<=\s))[a-zA-Z0-9]+[\w\.-]+@[a-zA-Z0-9]+[a-zA-Z0-9-]+\.[a-zA-Z]+(\.[a-zA-Z]+)?')

matches = email_expression.finditer(text)

for match in matches:
    print(match.group(0))