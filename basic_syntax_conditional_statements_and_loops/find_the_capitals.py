string = input()
listNum = []

for i in range(len(string)):
    if string[i].isupper():
        listNum.append(i)

print(listNum)