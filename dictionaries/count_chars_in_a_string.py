text = input()
count_chars = {}

for char in text:
    if char != " ":
        if char not in count_chars:
            count_chars[char] = 0
        count_chars[char] += 1

for char, count in count_chars.items():
    print(f"{char} -> {count}")


# Начин 2
from collections import Counter

word = input()
result = Counter(word)

for key, value in result.items():
    if key != " ":
        print(f"{key} -> {value}")