# def find_biggest_number(a: int, b: int) -> int:
#     return max(a, b)


def find_biggest_number(a: int, b: int) -> int:
    if a >= b:
        return a
    else:
        return b


print(find_biggest_number(100, 1))
print(find_biggest_number(100, 205))
print(find_biggest_number(6, 6))
