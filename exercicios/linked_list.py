from node import Node


"""
__get_node_at itera pela lista até chegar ao nó, portanto é O(n)

insert_at, insert_last, remove_last, remove_at e get_element_at
tem complexidade de tempo O(n) nessa implementação, já que utilizam a funcao
__get_node_at
"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.__length = 0

    def __str__(self):
        return f"LinkedList(len={self.__length}, value={self.head})"

    def __len__(self):
        return self.__length

    def __get_node_at(self, position):
        node_to_be_returned = self.head
        if node_to_be_returned:
            while position > 0 and node_to_be_returned.next:
                node_to_be_returned = node_to_be_returned.next
                position -= 1
        return node_to_be_returned

    def insert_first(self, value):
        first_value = Node(value)
        first_value.next = self.head
        self.head = first_value
        self.__length += 1

    def insert_last(self, value):
        if self.is_empty():
            return self.insert_first(value)

        new_last_value = Node(value)
        actual_last_value = self.__get_node_at(len(self) - 1)
        actual_last_value.next = new_last_value
        self.__length += 1

    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        current_value = self.__get_node_at(position - 1)
        next_value = Node(value)
        next_value.next = current_value.next
        current_value.next = next_value
        self.__length += 1

    def remove_first(self):
        value_to_be_removed = self.head
        if value_to_be_removed:
            self.head = self.head.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()

        previous_to_be_removed = self.__get_node_at(len(self) - 2)
        value_to_be_removed = previous_to_be_removed.next

        previous_to_be_removed.next = None
        self.__length -= 1
        return value_to_be_removed

    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self.__get_node_at(position - 1)

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next = None
        self.__length -= 1

        return value_to_be_removed

    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self.__get_node_at(position)
        if value_to_be_returned:
            value_returned = Node(value_to_be_returned.value)
        return value_returned

    def is_empty(self):
        return not self.__length

    def clear(self):
        while not self.is_empty():
            self.remove_first()


if __name__ == "__main__":
    linked_list = LinkedList()

    print(linked_list.is_empty())
    linked_list.insert_first(1)
    print(linked_list)

    linked_list.insert_first(2)
    print(linked_list)

    linked_list.insert_last(3)
    print(linked_list)

    linked_list.remove_last()
    print(linked_list)

    linked_list.remove_first()
    print(linked_list)

    linked_list.insert_at(5, 1)
    print(linked_list)

    linked_list.remove_at(0)
    print(linked_list)

    linked_list.insert_at(6, 1)
    linked_list.insert_at(7, 2)
    linked_list.insert_at(8, 3)
    linked_list.insert_at(9, 4)
    print(linked_list.get_element_at(3))
