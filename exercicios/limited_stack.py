from stack import Stack


class StackOverflow(Exception):
    pass


class LimitedStack(Stack):
    def __init__(self, limit):
        super().__init__()
        self._limit = limit

    # Complexidade O(1)
    def push(self, value):
        if len(self._data) + 1 > self._limit:
            raise StackOverflow
        return super().push(value)


if __name__ == "__main__":
    stack = LimitedStack(2)

    stack.push(1)
    stack.push(-2)

    print(stack)

    try:
        stack.push(3)
    except StackOverflow:
        print("Não é possível adicionar outro item à pilha")
