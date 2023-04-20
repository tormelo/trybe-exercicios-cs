def get_even_numbers_count(stop: int) -> int:
    even_numbers = 0

    for number in range(1, stop + 1):
        if number % 2 == 0:
            even_numbers += 1

    return even_numbers
