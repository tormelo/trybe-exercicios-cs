"""

Somando a complexidade de max que é O(n) com o laço O(n) o resultado parcial é
O(2n)

Simplificando e descartando a constante o resultado é
O(n)

A complexidade de espaço depende do tamanho da lista candies, ou seja, O(N)
"""


def kids_with_candies(candies, extra_candies):
    # parece que a solução percorre o array somente uma vez,
    # porém isto é feito duas vezes, uma no `max` e outra para
    # preencher a resposta
    max_candies = max(candies)
    return [candy + extra_candies >= max_candies for candy in candies]


# saída: [True, True, True, False, True]
print(kids_with_candies([2, 3, 5, 1, 3], 3))
