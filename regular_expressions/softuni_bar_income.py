# Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to go home and you are the person who has to draw the line
# and calculate the money from the products that were sold throughout the day. Until you receive a line with text "end of shift" you will be given lines of input. 
# But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# •	Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by lower-case letters
# •	Valid product contains any word character (not only letters) and must be surrounded by '<' and '>' 
# •	Valid count is an integer, surrounded by '|'
# •	Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}".


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
