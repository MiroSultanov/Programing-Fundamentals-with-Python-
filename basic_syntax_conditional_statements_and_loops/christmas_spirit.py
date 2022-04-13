quantity = int(input())
days = int(input())
christmas_spirit = 0
total_cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0 and day == days:
        christmas_spirit -= 30
    if day % 2 == 0:
        christmas_spirit += 5
        total_cost += quantity * 2
    if day % 3 == 0:
        christmas_spirit += 13
        total_cost += (5 * quantity) + (3 * quantity)
    if day % 5 == 0:
        christmas_spirit += 17
        total_cost += 15 * quantity
    if day % 3 == 0 and day % 5 == 0:
        christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += 3 + 5 + 15
print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")