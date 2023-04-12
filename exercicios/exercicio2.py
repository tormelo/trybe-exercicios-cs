import re


def decode_to_number(expression):
    if not 1 <= len(expression) <= 30:
        raise ValueError("Expression with invalid length")

    if re.findall(r"[^-01a-zA-Z]", expression):
        raise ValueError("Invalid character")

    table = [
        ("ABC", "2"),
        ("DEF", "3"),
        ("GHI", "4"),
        ("JKL", "5"),
        ("MNO", "6"),
        ("PQRS", "7"),
        ("TUV", "8"),
        ("WXYZ", "9"),
        ("-01", ""),
    ]

    number = ""
    for char in expression:
        for code, decode in table:
            if char in code:
                number += decode if decode else char

    return number
