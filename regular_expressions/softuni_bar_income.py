import re

total_sum = 0
expression = r"%([A-Z][a-z]+)%(?:[^\.\|\$%]+)?<(\w+)>(?:[^\.\|\$%]+)?\|(\d+)\|(?:[^\.\|\$%]+)?((?<=\D)\d+(?:\.\d+)?)(?=\$)\$$"

while True:
    input_data = input()
    if input_data == 'end of shift':
        break

    match = re.search(expression, input_data)

    if match:
        customer_name = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))
        total_price = count * price
        print(f"{customer_name}: {product} - {total_price:.2f}")
        total_sum += total_price
print(f"Total income: {total_sum:.2f}")