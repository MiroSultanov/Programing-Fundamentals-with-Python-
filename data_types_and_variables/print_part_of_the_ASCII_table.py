# Write a program that prints part of the ASCII table characters on the console, separated by a single space. 
# On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print. 

begin_char = int(input())
end_char = int(input())

for i in range(begin_char, end_char + 1):
    ascii_char = chr(i)
    print(ascii_char, end=' ')
