import re

input_data = input()

expressions = (r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))")

matches = re.finditer(expressions, input_data)

output = list()

for match in matches:
    output.append(match.group())
print(" ".join(output))