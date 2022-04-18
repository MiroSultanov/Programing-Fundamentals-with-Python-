def char_in_range(char_1, char_2):
    for i in range(ord(char_1) + 1, ord(char_2)):
        print(chr(i), end=' ')
char_1 = input()
char_2 = input()
char_in_range(char_1, char_2)