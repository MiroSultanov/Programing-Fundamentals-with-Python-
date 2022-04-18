# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that receives a list of positive integers, 
# separated by comma and space ", ". The function should check if each integer is a palindrome - True or False. Print the result.

def palindrome_func(nums):
    for num in nums:
        if num == num[::-1]:
            print("True")
        else:
            print("False")
numbers = input().split(', ')
palindrome_func(numbers)
