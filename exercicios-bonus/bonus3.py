def get_summation(limit: int):
    summation = 0
    for number in range(1, limit + 1):
        summation += number
    return summation


print(get_summation(5))
