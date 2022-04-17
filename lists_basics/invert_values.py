# Write a program that receives a single string containing positive and negative numbers separated by a single space. Print a list containing the opposite of each number.

nums = input().split(' ')
new_list = []

for num in nums:
    if int(num) > 0:
        new_list.append(-int(num))
    else:
        new_list.append(abs(int(num)))
print(new_list)
