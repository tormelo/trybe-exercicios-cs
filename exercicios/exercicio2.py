# from statistics import mean


# def find_mean(numbers: list) -> float:
#     return mean(numbers)


def find_mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)


numbers = [10, 5, 8, 4, 9, 5]

print(find_mean(numbers))
