def order_func(order_dict, command):
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product in order_dict:
        order_dict[product] = [price, (quantity + order_dict[product[1]])]
    else:
        order_dict[product]= [price, quantity]

    return order_dict

def orders():
    orders_dict = {}

    while True:
        command = input()
        if command == 'buy':
            break
        command = command.split(' ')
        orders_dict = order_func(orders_dict, command)

    for product in orders_dict:
        total_sum = orders_dict[product][0] * orders_dict[product][1]
        print(f"{product} -> {total_sum:.2f}")

orders()