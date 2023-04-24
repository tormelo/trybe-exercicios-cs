from random import shuffle
from utils.Cronometro import Cronometro


def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

    return numbers


def insertion_sort(numbers):
    for i in range(len(numbers)):
        current_value = numbers[i]
        current_index = i

        while current_index > 0 and numbers[current_index - 1] > current_value:
            numbers[current_index] = numbers[current_index - 1]
            current_index = current_index - 1

        numbers[current_index] = current_value

    return numbers


for input in (10000, 100000, 1000000):
    for algorithm in (insertion_sort, selection_sort):
        algorithm_name = algorithm.__name__

        sorted_numbers = list(range(input))
        reversed_sorted_numbers = list(reversed(sorted_numbers))
        random_numbers = sorted_numbers[:]  # copia dos ordenados
        shuffle(random_numbers)  # embaralha eles

        with Cronometro(
            f"{algorithm_name} com entrada ordenada de {input} números"
        ):
            algorithm(sorted_numbers)

        with Cronometro(
            f"{algorithm_name} com entrada"
            + f" inversamente ordenada de {input} números"
        ):
            algorithm(reversed_sorted_numbers)

        with Cronometro(
            f"{algorithm_name} com entrada aleatória de {input} números"
        ):
            algorithm(random_numbers)

        print("*" * 50)
