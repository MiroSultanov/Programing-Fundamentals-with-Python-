students_dict = {}

for _ in range(int(input())):
    name = input()
    grade = float(input())

    if name not in students_dict:
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)

for student, grade in students_dict.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")