from math import floor

first_number = int(input())
second_number = int(input())
third_number = int(input())
forth_number = int(input())

sum_1_2 = first_number + second_number
sum_3 = int(sum_1_2 / third_number)
sum_4 = sum_3 * forth_number
print(floor(sum_4))