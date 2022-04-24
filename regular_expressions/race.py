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

