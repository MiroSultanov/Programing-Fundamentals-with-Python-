# You will be given strings on separate lines until you receive an "end" command. Write a program that reverses strings and prints each pair on a separate line in the 
# format "{word} = {reversed_word}".

words = input()

while words != "end":
    rev = reversed(words)
    reversed_text = "".join(rev)
    print(f"{words} = {reversed_text}")
    words = input()
