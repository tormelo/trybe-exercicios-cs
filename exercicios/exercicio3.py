# Por conter um for dentro de outro a complexidade de tempo é O(n²)
def get_combinations_total(products: list[int]) -> int:
    combinations = 0
    size = len(products)

    for i in range(size):
        for j in range(i + 1, size):
            if products[i] == products[j]:
                combinations += 1

    return combinations


print(get_combinations_total([1, 3, 1, 1, 2, 3]))  # resultado = 4
print(get_combinations_total([1, 1, 2, 3]))  # resultado = 1
