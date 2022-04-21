# Write a program that keeps the information about students and their grades. 
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade. 
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.


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
