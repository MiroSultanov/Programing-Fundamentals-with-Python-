todo = ["" for i in range(11)]
command = input()

while command != 'End':
    xplode = command.split("-")
    priority = int(xplode[0])
    task = xplode[1]
    todo[priority] = task
    command = input()
final_todo = [task for task in todo if task != ""]
print(final_todo)