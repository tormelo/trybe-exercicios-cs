"""
A função length_of_longest_substring realiza dois laços um dentro
do outro e por isso sua Complexidade de Tempo é O(n²)
"""


def length_of_longest_substring(string):
    longest = 0

    start = 0
    end = len(string) - 1

    while start < end:
        substring = set()
        index = start

        while index < end:
            letter = string[index]
            if letter in substring:
                break
            substring.add(letter)
            index += 1

        if len(substring) > longest:
            longest = len(substring)

        start += 1

    return longest


if __name__ == "__main__":
    string = "serdevemuitolegalmasehprecisoestudarbastante"
    print(length_of_longest_substring(string))
