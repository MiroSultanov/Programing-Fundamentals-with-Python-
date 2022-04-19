# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. Print the new text string after removing the vowels. 
# The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

vowels = ["a", "o", "u", "e", "i"]
text = input()
no_vowels_text = (ch for ch in text if ch not in vowels)

print(''.join(no_vowels_text))
