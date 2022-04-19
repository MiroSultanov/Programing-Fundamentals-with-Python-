strings = input().split(', ')
sentence = input()
result = [el for el in strings if el in sentence]
print(result)
