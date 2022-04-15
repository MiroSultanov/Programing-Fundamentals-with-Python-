# Write a program, which sums the ASCII codes of N characters and prints the sum on the console. On the first line, you will receive N – the number of lines.
# On the following N lines – you will receive a letter per line. 
# Print the total sum in the following format: "The sum equals: {total_sum}".

num_lines = int(input())
sum = 0

for i in range(num_lines):
    char = str(input())
    sum += ord(char)

print(f"The sum equals: {sum}")
