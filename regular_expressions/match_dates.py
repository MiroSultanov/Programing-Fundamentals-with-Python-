import re

input_data = input()

expressions = (r"(?P<day>\d{2})([./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})")

matches = re.finditer(expressions, input_data)

for match in matches:
    day = match.group("day")
    month = match.group("Month")
    year = match.group("Year")

    print(f"Day: {day}, Month: {month}, Year: {year}")