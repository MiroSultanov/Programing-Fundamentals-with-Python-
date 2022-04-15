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