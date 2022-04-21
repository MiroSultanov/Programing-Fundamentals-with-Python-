resources = {}

while True:
    command = input()
    if command == "stop":
        break
    else:
        quantity = int(input())
        if command not in resources:
            resources[command] = 0
        resources[command] += quantity

for item, quantity in resources.items():
    print(f"{item} -> {quantity}")


resources = {}
command = input()

while command != 'stop':
    quantity = int(input())
    if command not in resources:
        resources[command] = 0
    resources[command] += quantity
    command = input()
for item, quantity in resources.items():
    print(f"{item} -> {quantity}")