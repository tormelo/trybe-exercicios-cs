def get_even_numbers_count(number: int) -> int:
    if number <= 1:
        return 0

    return (1 if number % 2 == 0 else 0) + get_even_numbers_count(number - 1)
