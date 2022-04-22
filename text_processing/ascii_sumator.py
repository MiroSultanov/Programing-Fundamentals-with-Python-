def ascii_simulator():
    char_1 = ord(input())
    char_2 = ord(input())
    input_data = input()

    sum_of_ascii = sum([ord(x) for x in input_data if char_1 < ord(x) < char_2])
    print(sum_of_ascii)

ascii_simulator()
