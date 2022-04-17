# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the cards in the two halves are perfectly interleaved, 
# such that the original bottom card is still on the bottom and the original top card is still on top. For example, faro shuffling the 
# list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six'] Write a program that receives a single string
# (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.


deck = input().split(' ')
shuffles = int(input())
middle_index = len(deck) // 2
first_half = deck[:middle_index]
second_half = deck[middle_index:]
new_deck = list()
for k in range(shuffles):
    new_deck.clear()
    for i in range(len(first_half)):
        new_deck.append(first_half[i])
        new_deck.append(second_half[i])
    first_half = new_deck[:middle_index]
    second_half = new_deck[middle_index:]
print(new_deck)
