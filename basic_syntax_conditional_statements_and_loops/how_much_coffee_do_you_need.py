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