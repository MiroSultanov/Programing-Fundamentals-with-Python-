# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines. 
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

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
