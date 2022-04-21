exam_submissions = {}
students = {}

while True:
    input_line = input()
    if input_line == 'exam finished':
        break

    command = input_line.split('-')
    username = command[0]
    language_action = command[1]

    if language_action != 'banned':
        if language_action not in exam_submissions:
            exam_submissions[language_action] = 0
        exam_submissions[language_action] += 1

        points = int(command[2])
        students[username] = max(students.get(username, 0), points)

    elif username in students:
        students.pop(username)

print('Results:')
for username, points in students.items():
    print(f"{username} | {points}")
print('Submissions:')
for language, submissions_count in exam_submissions.items():
    print(f'{language} - {submissions_count}')