from random import randint

"""
O problema é O(n), já que em caso de um valor de entrada alto a constante se
torna desprezível

A complexidade de espaço é constante, ou seja, O(1)
"""


def random_averages(n):
    list_of_averages = []

    for _ in range(100):
        average = 0
        for _ in range(n):
            average += randint(1, n)
        average = average / n
        list_of_averages.append(average)

    return list_of_averages
