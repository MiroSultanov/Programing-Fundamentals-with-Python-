def string_explosion(data):
    symbol = 0
    explosion = 0
    while symbol < len(data):
        char = data[symbol]
        if data[symbol] == ">":
            explosion += int(data[symbol + 1])
            symbol += 1
        elif explosion > 0:
            data = data[:symbol] + data[symbol + 1:]
            explosion -= 1
        else:
            symbol += 1
    print(data)

data = input()
string_explosion(data)