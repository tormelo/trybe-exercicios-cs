# def find_longest_name(names: list) -> str:
#     return max(names, key=len)


def find_longest_name(names: list) -> str:
    longest = ""
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest


names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

print(find_longest_name(names))
