budget = float(input())
price_per_floor = float(input())

for_one_bread = price_per_floor + (price_per_floor * 0.75) + ((price_per_floor * 1.25) / 4)
number_of_bread = 0
colored_eggs = 0

while budget > for_one_bread:
    budget -= for_one_bread
    number_of_bread += 1
    colored_eggs += 3
    if number_of_bread % 3 == 0:
        deduction = number_of_bread - 2
        colored_eggs -= deduction
money_left = abs(budget)
print(f"You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
