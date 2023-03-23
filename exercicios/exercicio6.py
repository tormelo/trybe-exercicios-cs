def get_triangle_type(a: float, b: float, c: float) -> str:
    if not (a + b > c and a + c > b and b + c > a):
        return "Não é triângulo"
    elif a == b == c:
        return "Triângulo Equilátero"
    elif a == b or a == c or b == c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


print(get_triangle_type(10, 10, 10))
print(get_triangle_type(10, 13, 10))
print(get_triangle_type(10, 13, 15))
print(get_triangle_type(10, 10, 22))
