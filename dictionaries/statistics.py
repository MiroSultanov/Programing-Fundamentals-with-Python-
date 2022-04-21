products = {}

while True:
    command = input()
    if command == "statistics":
        break

    else:
        element = command.split(": ")
        product = element[0]
        quantity = int(element[1])

        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

