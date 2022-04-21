elements = input().split(" ")
stock = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    stock[key] = int(value)

searched_stock = input().split(" ")
for product in searched_stock:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")