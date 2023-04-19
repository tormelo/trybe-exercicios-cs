"""

O pior, médio e melhor caso dependem da complexidade do algoritmo de 
ordenação do Python, que de acordo com a documentação tem complexidade
O(n log n)

Somando a ele a complexidade do laço O(n) o resultado parcial é
O(n + n log n)

Simplificando e descartando a menor complexidade o resultado é
O(n log n)

"""


def contains_duplicate(numbers):
    numbers.sort()
    previous_number = "not a number"
    for number in numbers:
        if previous_number == number:
            return True
        previous_number = number

    return False
