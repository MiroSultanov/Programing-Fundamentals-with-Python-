# Write a program that reads the path to a file and subtracts the file name and its extension.

def extract_file(data):
    needed_information = data[-1].split(".")
    file_name = needed_information[0]
    file_extension = needed_information[1]

    print(f"File name: {file_name}")
    print(f"File extension: {file_extension}")

data = input().split("\\")
extract_file(data)
