# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}". 
# Return a list containing all to-do notes sorted by importance in ascending order. 
# The importance value will always be an integer between 1 and 10 (inclusive).


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
