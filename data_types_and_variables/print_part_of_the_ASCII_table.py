begin_char = int(input())
end_char = int(input())

for i in range(begin_char, end_char + 1):
    ascii_char = chr(i)
    print(ascii_char, end=' ')