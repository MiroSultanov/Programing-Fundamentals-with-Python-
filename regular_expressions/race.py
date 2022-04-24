# Write a program that processes information about a race. On the first line you will be given list of participants separated by ", ". 
# On the next few lines until you receive a line "end of race" you will be given some info which will be some alphanumeric characters. 
# In between them you could have some extra characters which you should ignore. For example: "G!32e%o7r#32g$235@!2e". 
# The letters are the name of the person and the sum of the digits is the distance he ran. So here we have George who ran 29 km. 
# Store the information about the person only if the list of racers contains the name of the person. If you receive the same person more than once just add the 
# distance to his old distance. At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"


import re

racer_name = input()
result = {racer: 0 for racer in racer_name.split(", ")}

name_expression = re.compile(r"[A-Za-z]+")
distance_expression = re.compile(r"[0-9]")

while True:
    input_data = input()
    if input_data == "end of race":
        break

    name_match = name_expression.findall(input_data)
    distance_match = distance_expression.findall(input_data)

    if name_match and distance_match:
        name = "".join(name_match)
        distance = sum([int(x) for x in distance_match])

        if name in result.keys():
            result[name] += distance
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {sorted_result[0][0]}")
print(f"2nd place: {sorted_result[1][0]}")
print(f"3rd place: {sorted_result[2][0]}")

