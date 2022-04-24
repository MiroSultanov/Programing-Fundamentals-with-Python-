# Write a regular expression to match a valid phone number from Sofia. After you find all valid phones, print them on the console, separated by a comma and a space ", ".
# A valid number has the following characteristics:
# •	It starts with "+359"
# •	Then, it is followed by the area code (always 2)
# •	After that, it is followed by a number:
# o	The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively). 
# •	The different parts are separated by either a space or a hyphen ('-').


import re

phone_numbers = input()

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", phone_numbers)

output = list()

for match in matches:
    output.append(match.group())
print(", ".join(output))
