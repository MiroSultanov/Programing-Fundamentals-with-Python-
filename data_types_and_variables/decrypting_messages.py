key = int(input())
number_of_lines = int(input())
message = " "

for i in range(number_of_lines):
    letter = input()
    message = (ord(letter) + key )
    print(chr(message), end="")