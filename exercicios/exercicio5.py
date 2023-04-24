def binary_search(numbers, target):
    start_index = 0
    end_index = len(numbers) - 1

    while end_index >= start_index:
        mid_index = (end_index + start_index) // 2
        if target == numbers[mid_index]:
            return mid_index
        elif target < numbers[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    raise ValueError(f"{target} is not in the list")


numbers = [1, 10, 35, 38, 58, 59, 65, 73, 76, 98]

print(binary_search(numbers, 38))
