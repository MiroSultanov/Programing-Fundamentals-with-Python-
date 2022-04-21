phonebook = {}

while True:
    contact = input()
    if contact.isnumeric():
        break
    name, number = contact.split("-")
    phonebook[name] = number

for _ in range(int(contact)):
    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")