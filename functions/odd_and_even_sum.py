# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format: "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.


def odd_even_sum(nums):
    odd_sum = 0
    even_sum = 0
    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
numbers = map(int, list(input()))
odd_even_sum(numbers)
