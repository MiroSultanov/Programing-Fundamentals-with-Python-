# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each character with the corresponding character three positions
# forward in the ASCII table. For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

def caesar_cipher(data):
    output = [chr(ord(ch) + 3) for ch in data]
    print("".join(output))

data = input()
caesar_cipher(data)
