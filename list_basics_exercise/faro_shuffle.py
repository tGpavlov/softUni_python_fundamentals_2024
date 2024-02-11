cards_in_deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_of_deck = len(cards_in_deck) // 2
    left_side = cards_in_deck[:middle_of_deck]
    right_side = cards_in_deck[middle_of_deck:]
    shuffled_deck = []
    for cards in range(middle_of_deck):
        shuffled_deck.append(left_side[cards])
        shuffled_deck.append(right_side[cards])
    cards_in_deck = shuffled_deck

print(cards_in_deck)