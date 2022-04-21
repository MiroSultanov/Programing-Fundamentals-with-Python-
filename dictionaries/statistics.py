# You seem to be doing great at your first job, so your boss decides to give you as your next task something more challenging. You have to accept all the new products
# coming in the bakery and finally gather some statistics. You will be receiving key-value pairs on separate lines separated by ": " until you receive the command
# "statistics". Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"


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

