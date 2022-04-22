# Write a program that prints the sum of all found characters between two given characters (their ASCII code). On each of the first two lines, 
# you will receive a single character. On the last line, you get a random string. Print the sum of the ASCII values of all characters in the random string between 
# the two given characters in the ASCII table.

def ascii_simulator():
    char_1 = ord(input())
    char_2 = ord(input())
    input_data = input()

    sum_of_ascii = sum([ord(x) for x in input_data if char_1 < ord(x) < char_2])
    print(sum_of_ascii)

ascii_simulator()
