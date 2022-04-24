# Write a program that extracts links from a given text. The text will come in the form of strings, each representing a sentence. 
# You need to extract only the valid links from it.
# The Sub-Domain must always be "www". The Domain name can consist of English alphabet letters (uppercase and lowercase), digits, and dashes ("–"). 
# The Domain extension consists of one or more domain blocks, a domain block consists of a dot followed by one or more lowercase English alphabet letters, 
# a Domain extension must have at least one domain block in order to be valid. 
# The Sub-Domain and Domain name must be separated by a single dot. Any link that does NOT follow the specified above rules should be treated as invalid.

import re

expression = re.compile(r"www.[a-zA-Z0-9-]+(\.[a-z]+)+")

while True:
    input_data = input()
    if len(input_data) == 0:
        break

    matches = expression.finditer(input_data)
    for match in matches:
        print(match.group(0))
