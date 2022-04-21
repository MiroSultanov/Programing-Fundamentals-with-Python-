dictionary_syn = {}

for _ in range(int(input())):
    word = input()
    synonym = input()

    if word not in dictionary_syn:
        dictionary_syn[word] = [synonym]
    elif synonym not in dictionary_syn[word]:
        dictionary_syn[word].append(synonym)

for word, synonyms in dictionary_syn.items():
    print(f"{word} - {', '.join(synonyms)}")
