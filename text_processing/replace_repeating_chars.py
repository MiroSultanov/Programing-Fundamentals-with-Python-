input_data = input()
def replace_repeating_char(i):
    if i == len(input_data) - 1:
        return i + 1
    else:
        while input_data[i] == input_data[i + 1]:
            i += 1
            if i == len(input_data) - 1:
                break
    return i + 1

output = ""
i = 0
while i < len(input_data):
    output += input_data[i]
    i = replace_repeating_char(i)
else:
    print(output)