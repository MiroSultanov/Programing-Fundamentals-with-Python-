parking_lot_data = {}

for _ in range(int(input())):
    command = input().split(' ')
    action = command[0]
    user = command[1]

    if action == "register":
        license_plate_number = command[2]
        if user in parking_lot_data:
            print(f"ERROR: already registered with plate number {parking_lot_data.get(user)}")
        else:
            parking_lot_data[user] = license_plate_number
            print(f"{user} registered {license_plate_number} successfully")

    elif action == 'unregister':
        if user not in parking_lot_data:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            parking_lot_data.pop(user)

for username, license_plate_number in parking_lot_data.items():
    print(f"{username} => {license_plate_number}")