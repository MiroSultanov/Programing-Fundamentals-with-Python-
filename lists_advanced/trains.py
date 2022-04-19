num_wagons = int(input())
train = [0 for i in range(num_wagons)]
command = input()

while command != "End":
    xplode = command.split(' ')
    current_command = xplode[0]
    if current_command == 'add':
        num_people = int(xplode[1])
        train[-1] += num_people
    if current_command == "insert":
        position = int(xplode[1])
        num_people = int(xplode[2])
        train[position] += num_people
    if current_command == "leave":
        position = int(xplode[1])
        num_people = int(xplode[2])
        train[position] -= num_people
    command = input()
print(train)