# def data_type_func():
#     if data_type == "int":
#         print(number * 2)
#     elif data_type == "real":
#         print(f"{number * 1.5:.2f}")
#     elif data_type == 'string':
#         print()
#
# data_type = input()
# number = int(input())
# data_type_func()

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


