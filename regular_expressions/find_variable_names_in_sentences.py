import re

input_data = input()

expression = r"\b_[A-Za-z0-9]+\b"

matches = re.findall(expression, input_data)

output = list()

for match in matches:
    output.append(match[1:])
print(",".join(output))