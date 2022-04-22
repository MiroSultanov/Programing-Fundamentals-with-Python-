# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular. He asks for your help.
# He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3". You need to convert the 
# letters to uppercase for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for each string, there will be a
# corresponding number. The input will be given on a single line.


def rage_quit(input_string):
    word_list = []
    unique_chars = set()
    index = 0

    while index < len(input_string):
        if input_string[index].isnumeric():
            word = input_string[:index].upper()
            for ch in word:
                unique_chars.add(ch)

            i = index
            while input_string[i].isnumeric():
                i += 1
                if i == len(input_string):
                    break
            count = int(input_string[index:i])
            word_list.append((word, count))
            input_string = input_string[i:]
            index = 0
        else:
            index += 1
    else:
        print(f'Unique symbols used: {len(unique_chars)}')
        for word in word_list:
            print(word[0] * word[1], end='')

input_string = input()
rage_quit(input_string)
