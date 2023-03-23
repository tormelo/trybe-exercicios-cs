import math


def get_paint_cans_quantity_and_price(area: float) -> tuple:
    total_liters = area / 3
    required_cans = math.ceil(total_liters / 18)
    total_price = required_cans * 80
    return (required_cans, total_price)


print(get_paint_cans_quantity_and_price(45))
