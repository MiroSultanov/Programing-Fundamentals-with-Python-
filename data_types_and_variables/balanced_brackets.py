# On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
# •	Opening bracket – "(",
# •	Closing bracket – ")" or
# •	Random string
# Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. Nested parentheses are not valid,
# and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced. You should print "BALANCED" 
# if the parentheses are balanced and "UNBALANCED" otherwise.


number_lines = int(input())
last_bracket = ""
is_balanced = True

for line in range(number_lines):
    command = input()
    if command == "(" or command == ")":
        if command != last_bracket:
            last_bracket = command
        else:
            is_balanced = False
    else:
        pass
if is_balanced:
    print(f"BALANCED")
else:
    print(f"UNBALANCED")
