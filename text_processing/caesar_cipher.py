# text = input()
# output = "".join([chr(ord(x)+ 3) for x in text])
# print(output)

def caesar_cipher(data):
    output = [chr(ord(ch) + 3) for ch in data]
    print("".join(output))

data = input()
caesar_cipher(data)