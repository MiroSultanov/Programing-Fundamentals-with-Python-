word = input()
revers_word = ""

for i in range(len(word)-1, -1, -1):
    revers_word += word[i]
print(revers_word)