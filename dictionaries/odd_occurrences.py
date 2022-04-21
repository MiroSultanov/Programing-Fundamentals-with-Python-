# Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.


words = input().lower().split(" ")
dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1

output = [key for key, value in dictionary.items() if value % 2 != 0]
print(*output, sep=' ')
