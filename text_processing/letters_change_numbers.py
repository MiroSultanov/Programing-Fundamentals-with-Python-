# You receive a string consisting of a number between two letters. For the given string, you should perform different mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping track of only the total sum of all results. 
# Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind. 
# He kindly asks you to write a program that performs the operations described above and sums the final results of each string.



from string import ascii_lowercase


def extract_func(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = int(''.join(current_num)) * index
                else:
                    result = int(''.join(current_num)) / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index

    return result


def letters_change_numbers(data):
    result = 0

    for num in data:
        result += extract_func(num)

    print(f'{result:.2f}')


data = input().split()
letters_change_numbers(data)
