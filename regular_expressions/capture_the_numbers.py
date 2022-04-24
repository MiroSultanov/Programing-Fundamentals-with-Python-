# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers on a single line, separated by a single space.

import re

while True:
    input_data = input()
    if len(input_data) != 0:
        expressions = re.compile(r"\d+")
        matches = expressions.finditer(input_data)
        for match in matches:
            print(match.group(0), end=" ")
    else:
        break

