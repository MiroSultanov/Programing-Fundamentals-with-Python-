# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list of only the even numbers. Use filter().

result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
print(result)
