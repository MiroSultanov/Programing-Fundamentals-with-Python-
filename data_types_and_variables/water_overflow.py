# You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines, which will follow. 
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank. If the capacity is not enough, print "Insufficient capacity!" 
# and continue reading the next line. On the last line, print the liters in the tank.

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
