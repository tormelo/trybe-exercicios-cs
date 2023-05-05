from stack import Stack

"""
A complexidade é O(n), pois quanto mais tokens na expressão passada mais
operações serão feitas
"""


def solve_expression(expr):
    stack = Stack()
    tokens_list = expr.split(" ")

    for token in tokens_list:
        if token == "+":
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif token == "*":
            result = stack.pop() * stack.pop()
            stack.push(result)
        elif token == "-":
            num2 = stack.pop()
            num1 = stack.pop()
            result = num1 - num2
            stack.push(result)
        elif token == "/":
            num2 = stack.pop()
            num1 = stack.pop()
            result = num1 / num2
            stack.push(result)
        else:
            stack.push(int(token))

    return stack.pop()


# A = 5, B = 10, C = 30

# A + B - C / A -> 5 10 + 30 5 / -
print(solve_expression("5 10 + 30 5 / -"))  # 9

# B + (A * C) / C * 2 -> 10 5 30 * 30 / 2 * +
print(solve_expression("10 5 30 * 30 / 2 * +"))  # 20

# A * B - C + 4 * A - B -> 5 10 * 30 - 4 5 * 10 - +
print(solve_expression("5 10 * 30 - 4 5 * 10 - +"))  # 30

# (A + C / B ) * (A + B) -> 30 10 / 5 + 5 10 + *
print(solve_expression("30 10 / 5 + 5 10 + *"))  # 120

# 50 * B / 2 * 5 / A -> 50 10 * 2 / 5 * 5 /
print(solve_expression("50 10 * 2 / 5 * 5 /"))  # 250
