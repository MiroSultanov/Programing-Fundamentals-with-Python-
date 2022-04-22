def extract_name():
    name = None
    age = None
    for _ in range(n):
        input_data = input()
        data = input_data
        name_begin_index = data.find("@", None)
        if name_begin_index >= 0 and name_begin_index < len(data):
            data = data[name_begin_index + 1]
            name_end_index = data.find('|', None)
            if name_end_index > 0:
                name = data[:name_end_index]
        data = input_data

        age_begin_index = data.find("#", None)
        if age_begin_index >= 0 and age_begin_index < len(data):
            data = data[age_begin_index + 1]
            age_end_index = data.find("*", None)
            if age_end_index > 0:
                age = data[:age_end_index]

n = int(input())
