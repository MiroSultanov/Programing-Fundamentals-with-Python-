# Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code), 
# separated by a single space. Print the result on the console.

def char_in_range(char_1, char_2):
    for i in range(ord(char_1) + 1, ord(char_2)):
        print(chr(i), end=' ')
char_1 = input()
char_2 = input()
char_in_range(char_1, char_2)
