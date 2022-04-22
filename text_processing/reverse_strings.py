words = input()

while words != "end":
    rev = reversed(words)
    reversed_text = "".join(rev)
    print(f"{words} = {reversed_text}")
    words = input()
