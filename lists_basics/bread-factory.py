# As a young baker, you are baking the bread out of the bakery. 
# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. Each event is separated with '|' (vertical bar): 
# "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# •	If the event is "rest":
# o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You gained {gained_energy} energy.". 
# o	After that, print your current energy: "Current energy: {current_energy}.".
# •	If the event is "order": 
# o	You've earned some coins (the number in the second part). 
# o	Each time you get an order, your energy decreases by 30 points.
# 	If you have the energy to complete the order, print: "You earned {earned} coins.".
# 	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend. 
# o	If you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. 
# If you managed to handle all events through the day, print on the following 3 lines: 
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"


events = input().split('|')
energy = 100
coins = 100
close_condition = False

for event in events:
    current_event_element = event.split('-')
    command = current_event_element[0]
    number = int(current_event_element[1])

    if command == 'rest':
        if energy >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif command == 'order':
        if energy >= 30:
            print(f"You earned {number} coins.")
            energy -= 30
            coins += number
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            print(f"You bought {command}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {command}.")
            close_condition = True
            break
if not close_condition:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
