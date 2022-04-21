# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end". 
# You should register each user into the corresponding course. If the given course does not exist, add it. 
# When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.


courses = {}

while True:
    input_line = input()
    if input_line == 'end':
        break

    course_name, student_name = input_line.split(' : ')
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course_name in courses.keys():
    students = courses.get(course_name)
    registered_students = len(students)
    print(f"{course_name}: {registered_students}")
    formated_students = [f"-- {name}" for name in students]
    print(*formated_students, sep='\n')
