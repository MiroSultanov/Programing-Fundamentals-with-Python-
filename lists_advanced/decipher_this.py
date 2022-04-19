numbers = '0123456789'
index_num = lambda x: max(i for i in range(len(x)) if x[i]in numbers)

list_word = input().split(" ")
list =[]

for word in list_word:
    num = word[:index_num(word) + 1]
    first_char = chr(int(num))
    new_word = first_char + word[len(num):]
    if len(new_word) > 2:
        new_word = new_word[0:1] + new_word[-1] + new_word[2:-1] + new_word[1]

    list.append(new_word)
print(" ".join(list))
