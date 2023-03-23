def get_fuel_total_price(liters: float, type: str) -> float:
    liter_price = {"A": 1.90, "G": 2.50}
    discount_rates = {
        "min": {"A": 0.03, "G": 0.04},
        "max": {"A": 0.05, "G": 0.06},
    }

    discount_rate = 0

    if liters > 20:
        discount_rate = discount_rates["max"][type]
    else:
        discount_rate = discount_rates["min"][type]

    return liter_price[type] * liters * (1 - discount_rate)


print(get_fuel_total_price(50, "A"))
print(get_fuel_total_price(18, "A"))
print(get_fuel_total_price(50, "G"))
print(get_fuel_total_price(18, "G"))
