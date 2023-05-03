# Por conta do for a complexidade de tempo é O(n)
def get_max_uptime(states: list[int]) -> int:
    max_uptime = 0
    uptime = 0

    for state in states:
        if uptime > max_uptime:
            max_uptime = uptime

        if state == 1:
            uptime += 1
        else:
            uptime = 0

    return max_uptime


print(get_max_uptime([0, 1, 1, 1, 0, 0, 1, 1]))  # resultado = 3
print(get_max_uptime([1, 1, 1, 1, 0, 0, 1, 1]))  # resultado = 4
