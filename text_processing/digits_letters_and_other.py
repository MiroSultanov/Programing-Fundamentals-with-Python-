text = input()
digit = ""
letters = ""
symbols = ""

for ch in text:
    if ch.isdigit():
        digit += ch
    elif ch.isalpha():
        letters += ch
    else:
        symbols += ch
print(digit)
print(letters)
print(symbols)