# You will receive a string with even integers, separated by a "@" - this is our neighborhood. After that, a series of Jump commands will follow until 
# you receive "Love!". Every house in the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate
# Valentine's Day. The integers in the neighborhood indicate those needed hearts.
# Cupid starts at the position of the first house (index 0) and must jump by a given length. The jump commands will be in this format: "Jump {length}". 
# Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2: 
# •	If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has Valentine's day." 
# •	If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
# •	Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and if he does jump outside of it, he should start from the 
# first house again (index 0)



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
