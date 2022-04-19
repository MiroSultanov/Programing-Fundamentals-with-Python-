house_list = [int(x) for x in input().split('@')]

index = 0
while True:
    command = input()

    if command == 'Love!':
        break
    else:
        jump = int(list(command.split(' '))[1])
        index += jump
        if index >= len(house_list):
            index = 0
        if house_list[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            house_list[index] -= 2
            if house_list[index] == 0:
                print(f"Place {index} has Valentine's day.")

print(f"Cupid's last position was {index}.")
if sum(house_list) == 0:
    print('Mission was successful.')
else:
    failed_houses = [x for x in house_list if x != 0]
    print(f'Cupid has failed {len(failed_houses)} places.')