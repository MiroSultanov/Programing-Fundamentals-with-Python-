numbers = input().split(', ')
num = list(map(int, numbers))
even_index_num = list()

for i in range(len(num)):
    if num[i] % 2 == 0:
        even_index_num.append(i)

print(even_index_num)