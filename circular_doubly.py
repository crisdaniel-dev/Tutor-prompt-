from node import Node


class CircularDoubly:

    def __init__(self):
        self.__head = self.__tail = None

    def add_first(self, data):
        node = Node(data)

        if self.__head:
            node.next = self.__head
            node.prev = self.__tail

            self.__head.prev = node
            self.__tail.next = node

            self.__head = node
        else:
            self.__head = self.__tail = node
            node.next = node.prev = node

    def add_last(self, data):
        node = Node(data)

        if self.__head:
            node.prev = self.__tail
            node.next = self.__head

            self.__tail.next = node
            self.__head.prev = node

            self.__tail = node
        else:
            self.__head = self.__tail = node
            node.next = node.prev = node

    def add_after(self, data, key):
        assert self.__head, "List is empty"

        current = self.__head

        while True:
            if current.data == key:
                node = Node(data)

                node.next = current.next
                node.prev = current

                current.next.prev = node
                current.next = node

                if current is self.__tail:
                    self.__tail = node

                return

            current = current.next

            if current is self.__head:
                break

        raise ValueError("Key not found")

    def add_before(self, data, key):
        assert self.__head, "List is empty"

        current = self.__head

        while True:
            if current.data == key:
                node = Node(data)

                node.prev = current.prev
                node.next = current

                current.prev.next = node
                current.prev = node

                if current is self.__head:
                    self.__head = node

                return

            current = current.next

            if current is self.__head:
                break

        raise ValueError("Key not found")

    def del_first(self):
        assert self.__head, "List is empty"

        if self.__head is self.__tail:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next

            self.__head.prev = self.__tail
            self.__tail.next = self.__head

    def del_last(self):
        assert self.__head, "List is empty"

        if self.__head is self.__tail:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev

            self.__tail.next = self.__head
            self.__head.prev = self.__tail

    def del_given(self, key):
        assert self.__head, "List is empty"

        current = self.__head

        while True:
            if current.data == key:

                if current is self.__head:
                    if self.__head is self.__tail:
                        self.__head = self.__tail = None
                    else:
                        self.__head = self.__head.next

                        self.__head.prev = self.__tail
                        self.__tail.next = self.__head

                elif current is self.__tail:
                    self.__tail = self.__tail.prev

                    self.__tail.next = self.__head
                    self.__head.prev = self.__tail

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return

            current = current.next

            if current is self.__head:
                break

        raise ValueError("Key not found")

    def del_even(self):
        assert self.__head, "List is empty"

        current = self.__head
        original_head = self.__head

        while True:
            next_node = current.next

            if current.data % 2 == 0:

                if current is self.__head:
                    if self.__head is self.__tail:
                        self.__head = self.__tail = None
                        return
                    else:
                        self.__head = self.__head.next

                        self.__head.prev = self.__tail
                        self.__tail.next = self.__head

                elif current is self.__tail:
                    self.__tail = self.__tail.prev

                    self.__tail.next = self.__head
                    self.__head.prev = self.__tail

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

            if self.__head is None:
                return

            current = next_node

            if current is original_head:
                break

    def delete_greater(self, key):
        assert self.__head, "List is empty"

        current = self.__head
        original_head = self.__head

        while True:
            next_node = current.next

            if current.data > key:

                if current is self.__head:
                    if self.__head is self.__tail:
                        self.__head = self.__tail = None
                        return
                    else:
                        self.__head = self.__head.next

                        self.__head.prev = self.__tail
                        self.__tail.next = self.__head

                elif current is self.__tail:
                    self.__tail = self.__tail.prev

                    self.__tail.next = self.__head
                    self.__head.prev = self.__tail

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

            if self.__head is None:
                return

            current = next_node

            if current is original_head:
                break

    def length(self):
        length = 0

        if self.__head is None:
            return length

        current = self.__head

        while True:
            length += 1
            current = current.next

            if current is self.__head:
                break

        return length

    def total(self):
        total = 0

        if self.__head is None:
            return total

        current = self.__head

        while True:
            total += current.data
            current = current.next

            if current is self.__head:
                break

        return total

    def largest(self):
        assert self.__head, "List is empty"

        largest = self.__head.data
        current = self.__head.next

        while current is not self.__head:
            if current.data > largest:
                largest = current.data

            current = current.next

        return largest

    def smallest(self):
        assert self.__head, "List is empty"

        smallest = self.__head.data
        current = self.__head.next

        while current is not self.__head:
            if current.data < smallest:
                smallest = current.data

            current = current.next

        return smallest

    def count_occur(self, key):
        count = 0

        if self.__head is None:
            return count

        current = self.__head

        while True:
            if current.data == key:
                count += 1

            current = current.next

            if current is self.__head:
                break

        return count

    def reverse(self):
        if self.__head is None:
            return CircularDoubly()

        new_list = CircularDoubly()
        current = self.__tail

        while True:
            node = Node(current.data)

            if new_list.__head is None:
                new_list.__head = new_list.__tail = node
                node.next = node.prev = node
            else:
                node.next = new_list.__head
                node.prev = new_list.__tail

                new_list.__tail.next = node
                new_list.__head.prev = node

                new_list.__tail = node

            current = current.prev

            if current is self.__tail:
                break

        return new_list

    def sort_asc(self):
        if self.__head is None:
            return

        current = self.__head

        while True:
            index = current.next

            while index is not self.__head:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data

                index = index.next

            current = current.next

            if current is self.__tail:
                break

    def sort_desc(self):
        if self.__head is None:
            return

        current = self.__head

        while True:
            index = current.next

            while index is not self.__head:
                if current.data < index.data:
                    current.data, index.data = index.data, current.data

                index = index.next

            current = current.next

            if current is self.__tail:
                break

    def display(self):
        assert self.__head, "List is empty"

        current = self.__head
        output = ""

        while True:
            output += str(current.data) + " "
            current = current.next

            if current is self.__head:
                break

        return output.strip()
