# Tony and Andi love playing in the snow and having snowball fights, but they always argue about which makes the best snowballs. 
# They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.


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
