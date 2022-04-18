# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".
# Print the result on the console.


def data_type_func():
    if data_type == 'int':
        print(int(number) * 2)
    elif data_type == "real":
        print(f"{float(number) * 1.5:.2f}")
    elif data_type == "string":
        print(f"${number}$")

data_type = input()
number = input()
data_type_func()


