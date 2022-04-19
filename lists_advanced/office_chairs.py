def office_chairs(number_room):
    chairs_left = 0
    condition = True

    for room_number in range(1, number_room + 1):
        data = input().split(' ')
        available_chairs = data[0]
        visitors = int(data[1])

        difference = abs(len(available_chairs) - visitors)
        if len(available_chairs) < visitors:
            condition = False
            print(f"{difference} more chairs needed in room {room_number}")

        elif len(available_chairs) > visitors:
            chairs_left += difference

    if condition:
        print(f"Game On, {chairs_left} free chairs left")

info = int(input())
office_chairs(info)



