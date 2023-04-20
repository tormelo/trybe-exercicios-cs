def get_biggest_number(numbers: list[int]) -> int:
    if len(numbers) <= 1:
        return numbers[0]

    curr = numbers[0]
    next = get_biggest_number(numbers[1:])

    return curr if curr > next else next
