# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. Finally, print all items with
# their names and the total price of each product. 


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
