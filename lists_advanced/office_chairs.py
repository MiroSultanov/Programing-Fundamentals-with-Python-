# You are a facility manager at a large business center. One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center. On the following n lines for each room, you will
# receive information about the chairs in the room and the number of visitors. Each chair will be presented with the char "X". Next, there will be a single space
# and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors). 
# Keep track of the free chairs:
# •	If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". 
#     The rooms start from 1.
# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".


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



