# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines, you will be given some strings. 
# You should add them to a list and print them. After that, you should filter out only the strings that include the given word and print that list too.

numbers = int(input())
search_word = input()
filtered = list()
string = list()

for i in range(numbers):
    current_word = input()
    string.append(current_word)
    if search_word in current_word:
        filtered.append(current_word)
print(string)
print(filtered)




# number = int(input())
# word = input()
# string = []
#
# for i in range(number):
#     current_string = input()
#     string.append(current_string)
# print(string)
#
# for i in range(len(string) -1, -1, -1):
#     element = string[i]
#     if word not in element:
#         string.remove(element)
# print(string)
