# Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even. Print each word on a new line.

data = input().split(' ')
result = [word for word in data if len(word) % 2 == 0]
print("\n".join(result))
