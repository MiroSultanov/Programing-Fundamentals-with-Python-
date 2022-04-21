courses = {}

while True:
    input_data = input().split(":")
    if len(input_data) == 1:
        course = input_data[0]
        break
    else:
        name = input_data[0]
        id = input_data[1]
        course = "_".join(input_data[2].split(" "))

    if course not in courses:
        courses[course] = []
    courses[course].append(f"{name} - {id}")

output = courses[course]
print(*output, sep= '\n')

