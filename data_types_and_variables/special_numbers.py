# Write a program that reads an integer n. Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False). 
# A number is special when the sum of its digits is 5, 7, or 11.

number = int(input())

for num in range(1, number + 1):
    sum_of_digits = 0
    digit = num
    while digit > 0:
        sum_of_digits += digit % 10
        digit = int(digit / 10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
