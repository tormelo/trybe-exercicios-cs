# Por conter um único for a complexidade de tempo é O(n)
def get_students_at_time(
    arrivals: list[int], departures: list[int], target_time: int
) -> int:
    matches = 0

    for i in range(len(arrivals)):
        if arrivals[i] <= target_time <= departures[i]:
            matches += 1

    return matches


print(get_students_at_time([1, 2, 3], [3, 2, 7], 1))  # resultado = 1
