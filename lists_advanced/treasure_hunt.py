loot = input().split("|")
while True:
    input_line = input()
    if input_line == 'Yohoho!':
        break

    tokens = input_line.split(' ')
    command = tokens[0]

    if command == 'Loot':
        items = [x for i, x in enumerate(tokens) if i != 0 and x not in loot]
        items.reverse()
        loot = items + loot

    elif command == 'Drop':
        i = int(tokens[1])
        if 0 <= i < len(loot):
            loot.append(loot.pop(i))

    elif command == 'Steal':
        i = int(tokens[1])
        if i > len(loot):
            print(*loot, sep=', ')
            loot.clear()
        else:
            print(*loot[-i:], sep=', ')
            loot = loot[:-i]

if loot:
    gain = sum([len(x) for x in loot]) / len(loot)
    print(f"Average treasure gain: {gain:.2f} pirate credits.")

else:
    print("Failed treasure hunt.")