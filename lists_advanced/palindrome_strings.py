# On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome. 
# First, you should print a list containing all the found palindromes in the sequence. 
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

words = input().split(" ")
palindrome_words = list()
palindrome = input()

for word in words:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindrome_words.append(word)

print(palindrome_words)
palindrome_count = words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")
