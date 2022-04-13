# Everybody knows that you spend too much time awake during nighttime.
# Your task is to define how much coffee you need to stay awake. Until you receive the command "END", you need to read commands on different lines. 
# According to the commands, you will print the number of coffees you need to stay awake during the daytime. If the count exceeds 5, print 'You need extra sleep'.
# The list of events can contain the following:
# You have homework to do ("coding").
# You have a dog or a cat that just decided to wake up too early ("dog" or "cat").
# You watch a movie ("movie").
# If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase. If it is lowercase, you need 1 coffee by event, and if it is uppercase, you need 2 coffees.


command = input()
key_words = 'dog, cat, movie, coding'
counter_coffee = 0

while command != "END":
    if command in key_words.upper():
        counter_coffee += 2
    elif command in key_words.lower():
        counter_coffee += 1
    else:
        counter_coffee += 0
    command = input()
if counter_coffee > 5:
    print(f"You need extra sleep")
else:
    print(counter_coffee)
