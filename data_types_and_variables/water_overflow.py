n = int(input())
water_tank = 255
capacity = 0

for litters in range(n):
    litters = int(input())
    if capacity + litters <= water_tank:
        capacity += litters
        continue
    print(f"Insufficient capacity!")
print(capacity)
