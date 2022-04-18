# Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use an appropriate name for the function

def smallest_number(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c

current_a = int(input())
current_b = int(input())
current_c = int(input())

print(smallest_number(current_a, current_b, current_c))

