number_of_snowballs = int(input())
max_value_of_snowballs = 0
count_snowball_weight = 0
count_snowball_time = 0
count_snowball_quality = 0

for i in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > max_value_of_snowballs:
        max_value_of_snowballs = snowball_value
        count_snowball_weight = snowball_weight
        count_snowball_time = snowball_time
        count_snowball_quality = snowball_quality

print(f"{count_snowball_weight} : {count_snowball_time} = {max_value_of_snowballs:.0f} ({count_snowball_quality})")
