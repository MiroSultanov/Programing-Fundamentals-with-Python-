gift_list = input().split(' ')

data = input()
while data != 'No Money':
    command = data.split(' ')
    action = command[0]
    gift = command[1]

    if action == 'OutOfStock':
        gift_list[:] = ['None' if item == gift else item for item in gift_list]

    elif action == 'Required':
        gift_index = int(command[2])
        if 0 < gift_index < len(gift_list):
            gift_list[gift_index] = gift

    elif action == 'JustInCase':
        gift_list.pop()
        gift_list.append(gift)

    data = input()

else:
    if len(gift_list) > 0:
        res = ''
        for gift in gift_list:
            if gift != 'None':
                res += gift + ' '
        print(res)