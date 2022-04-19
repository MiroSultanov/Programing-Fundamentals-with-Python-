targets = list(map(int, input().split(" ")))

while True:
    command = input()
    if command == "End":
        break

    current_command = command.split(" ")
    action = current_command[0]
    index = int(current_command[1])
    value = int(current_command[2])

    if current_command[0] == "Shoot":
        if 0 <= index <= len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif current_command[0] == "Add":
        if 0 <= index <= len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif current_command[0] == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = [targets[i] for i in range(len(targets)) if not (index - value <= i <= index + value)]
        else:
            print("Strike missed!")

output = '|'.join([str(x) for x in targets])
print(output)



