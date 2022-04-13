# Write a program that takes a single string and prints a list of all the capital letters indices.

string = input()
listNum = []

for i in range(len(string)):
    if string[i].isupper():
        listNum.append(i)

print(listNum)
