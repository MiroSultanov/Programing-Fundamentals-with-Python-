# import re
#
# phone_numbers = input()
#
# matches = re.findall(r"\+359 2 \d{3} \d{4}\b| \+359-2-\d{3}-\d{4}\b", phone_numbers)
#
# print(",".join(matches))

import re

phone_numbers = input()

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", phone_numbers)

output = list()

for match in matches:
    output.append(match.group())
print(", ".join(output))