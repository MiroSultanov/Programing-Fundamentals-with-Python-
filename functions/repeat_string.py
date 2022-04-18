# Write a function that receives a string and a counter n. The function should return a new string – the result of repeating the old string n times. 
# Print the result of the function. Try using lambda.

repeater = lambda str, counter: str * counter
current_string = input()
current_counter = int(input())
print(repeater(current_string, current_counter))
