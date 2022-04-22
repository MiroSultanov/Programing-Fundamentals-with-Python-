# Write a program that reads a string from the console that contains:
# •	Explosions marked with '>'
# •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# •	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>') while deleting characters, 
# you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string. 


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
