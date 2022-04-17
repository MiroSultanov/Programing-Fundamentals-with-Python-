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
