# Write a function that receives two integer numbers. Calculate the factorial of each number. 
# Divide the first result by the second and print the division formatted to the second decimal point.


def factorial_func(num):
    return 1 if num == 0 or num == 1 else num * factorial_func(num - 1)

num_1 = int(input())
num_2 = int(input())
result = factorial_func(num_1) / factorial_func(num_2)
print(f"{result:.2f}")
