# import string
#
# valid_chars = [ch for ch in list(string.printable) if ch.isalnum() or ch in ("-","_")]
#
# lenght_chars = lambda x: True if 3 < len(x) <= 16 else False
#
# invalid_chars = lambda x: True if list(filter(lambda ch: ch not in valid_chars, x)) else False
#
# usernames = input().split(", ")
# for names in usernames:
#     if lenght_chars(names) and not invalid_chars(names):
#         print(names)
import string


def valid_usernames(data):
    flag = 0
    elements = string.digits + string.ascii_letters + "_" + "-"

    for name in data:
        flag = 0
        if 3 > len(name) or len(name) >= 16:
            flag = 1
        elif len([x for x in name if x in elements]) != len(name):
            flag = 1
        elif flag == 0:
            print(name)

input_data = input().split(", ")
valid_usernames(input_data)
