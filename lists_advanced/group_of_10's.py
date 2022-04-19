# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers sorted
# into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.


from math import ceil

input_data = list(map(int, input().split(', ')))

for num in range(1, ceil(max(input_data)/ 10) + 1):
    group_nums = list(filter(lambda n: (num - 1) * 10 < n <= num * 10, input_data))
    print(f"Group of {num}0's: {group_nums}")
