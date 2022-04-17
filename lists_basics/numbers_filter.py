# On the first line, you will receive a single number n. On the following n lines, you will receive integers. After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.


n = int(input())
even = list()
odd = list()
positive = list()
negative = list()

for i in range(n):
    current_num = int(input())
    if current_num % 2 == 0:
        even.append(current_num)
    else:
        odd.append(current_num)
    if current_num >= 0:
        positive.append(current_num)
    else:
        negative.append(current_num)

filter_word = input()
# може редовете от 21 до 28 да се изтрият и да се напише:
# print(eval(filter_word))

if filter_word == 'even':
    print(even)
if filter_word == "odd":
    print(odd)
if filter_word == "positive":
    print(positive)
if filter_word == 'negative':
    print(negative)

