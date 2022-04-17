numbers = input().split(' ')
copy_nums = list(map(int, numbers))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    numbers.remove(str(current_min_element))
    copy_nums.remove(current_min_element)
print(', '.join(numbers))