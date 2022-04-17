# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide to buy some items with your budget 
# and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value.
# If you don't have enough money for it, you can't buy it. Buy as many items as you can. Next, you should increase the price of each item you have successfully 
# bought by 40% and then sell it. Calculate if the budget after selling all the items is enough for buying the train ticket.


items = input().split('|')
budget = int(input())
profit = 0
new_item_prices = []
data_prices = []
condition = False

for item in items:
    current_item_info = item.split('->')
    type_of_product = current_item_info[0]
    price = float(current_item_info[1])
    condition = False

    if type_of_product == "Clothes":
        if price <= 50:
            condition = True
    elif type_of_product == "Shoes":
        if price <= 35:
            condition = True
    elif type_of_product == 'Accessories':
        if price <= 20.50:
            condition = True
    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            new_price = price + (price * 0.40)
            new_item_prices.append(new_price)
            data_prices.append(f'{new_price:.2f}')
print(' '.join(data_prices))
print(f"Profit: {profit:.2f}")

total_sum = budget + sum(new_item_prices)
if total_sum >= 150:
    print('Hello, France!')
else:
    print("Not enough money.")
