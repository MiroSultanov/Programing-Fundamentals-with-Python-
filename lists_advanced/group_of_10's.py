from math import ceil

input_data = list(map(int, input().split(', ')))

for num in range(1, ceil(max(input_data)/ 10) + 1):
    group_nums = list(filter(lambda n: (num - 1) * 10 < n <= num * 10, input_data))
    print(f"Group of {num}0's: {group_nums}")