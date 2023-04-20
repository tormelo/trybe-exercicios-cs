def get_greatest_common_divisor(a: int, b: int) -> int:
    if b == 0:
        return a
    return get_greatest_common_divisor(b, a % b)
