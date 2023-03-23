# def find_smallest_number(numbers: list) -> int:
#     return min(numbers)


def find_smallest_number(numbers: list) -> int:
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]

print(find_smallest_number(numbers))
