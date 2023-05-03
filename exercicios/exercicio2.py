# Por conta do for a complexidade de tempo é O(n)
def shuffle_cards(cards: list[int]) -> list[int]:
    shuffled_cards = []
    distance = len(cards) // 2

    for i in range(distance):
        shuffled_cards.extend(cards[i::distance])

    return shuffled_cards


print(shuffle_cards([2, 6, 4, 5]))  # resultado = [2, 4, 6, 5]
print(shuffle_cards([1, 4, 4, 7, 6, 6]))  # resultado = [1, 7, 4, 6, 4, 6]
