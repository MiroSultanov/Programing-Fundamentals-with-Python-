# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n represents the count of numbers
# to remove from the list. You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

numbers = input().split(' ')
copy_nums = list(map(int, numbers))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    numbers.remove(str(current_min_element))
    copy_nums.remove(current_min_element)
print(', '.join(numbers))
