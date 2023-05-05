class Stack:
    def __init__(self):
        self._data = []

    def __str__(self):
        return str(self._data)

    def push(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self):
        return not len(self._data)


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack)

    stack.pop()

    print(stack)

    print(stack.peek())
