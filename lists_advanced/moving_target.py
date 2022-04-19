# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first line, you will receive a sequence of
# targets with their integer values, split by a single space. Then, you will start receiving commands for manipulating the targets until the "End" command. 
# The commands are the following:
# •	"Shoot {index} {power}"
# o	Shoot the target at the index if it exists by reducing its value by the given power (integer value). A target is considered shot when its value reaches 0.
# o	Remove the target if it is shot.
# •	"Add {index} {value}"
# o	Insert a target with the received value at the received index if it exists. If not, print: "Invalid placement!"
# •	"Strike {index} {radius}"
# o	Remove the target at the given index (if such exist) and the ones before and after it depending on the radius. 
# o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
#  Example:  "Strike 2 2"
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}		

# •	"End"
# o	Print the sequence with targets in the following format:
# "{target1}|{target2} … |{targetn}"


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



