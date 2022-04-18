def factorial_func(num):
    return 1 if num == 0 or num == 1 else num * factorial_func(num - 1)

num_1 = int(input())
num_2 = int(input())
result = factorial_func(num_1) / factorial_func(num_2)
print(f"{result:.2f}")