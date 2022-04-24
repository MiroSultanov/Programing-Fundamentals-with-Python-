import re

expression = re.compile(r"www.[a-zA-Z0-9-]+(\.[a-z]+)+")

while True:
    input_data = input()
    if len(input_data) == 0:
        break

    matches = expression.finditer(input_data)
    for match in matches:
        print(match.group(0))