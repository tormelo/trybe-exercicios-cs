def fizzbuzz(stop: int) -> list[str | int]:
    result_list = []
    for number in range(1, stop + 1):
        result = ""
        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        result_list.append(result if result else number)

    return result_list
