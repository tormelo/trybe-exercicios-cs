from linked_list import LinkedList


class Queue:
    def __init__(self):
        self._data = LinkedList()

    def enqueue(self, value):
        self._data.insert_last(value)

    def dequeue(self):
        return self._data.remove_first()

    def peek(self):
        return self._data.get_element_at(0)

    def is_empty(self):
        return self._data.is_empty()


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.peek())
