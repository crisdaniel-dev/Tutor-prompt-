from node import Node


class Doubly:

    def __init__(self):
        self.__head = self.__tail = None

    def add_first(self, data):
        node = Node(data)

        if self.__head:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        else:
            self.__head = self.__tail = node

    def add_last(self, data):
        node = Node(data)

        if self.__head:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node
        else:
            self.__head = self.__tail = node

    def add_after(self, data, key):
        assert self.__head, "List is empty"

        current = self.__head

        while current:
            if current.data == key:
                node = Node(data)

                node.next = current.next
                node.prev = current

                if current.next:
                    current.next.prev = node
                else:
                    self.__tail = node

                current.next = node
                return

            current = current.next

        raise ValueError("Key not found")

    def add_before(self, data, key):
        assert self.__head, "List is empty"

        if self.__head.data == key:
            node = Node(data)

            node.next = self.__head
            self.__head.prev = node
            self.__head = node
            return

        current = self.__head

        while current:
            if current.data == key:
                node = Node(data)

                node.prev = current.prev
                node.next = current

                current.prev.next = node
                current.prev = node
                return

            current = current.next

        raise ValueError("Key not found")

    def del_first(self):
        assert self.__head, "List is empty"

        if self.__head is self.__tail:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None

    def del_last(self):
        assert self.__head, "List is empty"

        if self.__head is self.__tail:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None

    def del_given(self, key):
        assert self.__head, "List is empty"

        current = self.__head

        while current:
            if current.data == key:

                if current is self.__head:
                    if self.__head is self.__tail:
                        self.__head = self.__tail = None
                    else:
                        self.__head = self.__head.next
                        self.__head.prev = None

                elif current is self.__tail:
                    self.__tail = self.__tail.prev
                    self.__tail.next = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return

            current = current.next

        raise ValueError("Key not found")

    def length(self):
        count = 0
        current = self.__head

        while current:
            count += 1
            current = current.next

        return count

    def total(self):
        total = 0
        current = self.__head

        while current:
            total += current.data
            current = current.next

        return total

    def largest(self):
        assert self.__head, "List is empty"

        largest = self.__head.data
        current = self.__head.next

        while current:
            if current.data > largest:
                largest = current.data

            current = current.next

        return largest

    def smallest(self):
        assert self.__head, "List is empty"

        smallest = self.__head.data
        current = self.__head.next

        while current:
            if current.data < smallest:
                smallest = current.data

            current = current.next

        return smallest

    def reverse(self):
        new_list = Doubly()

        current = self.__tail

        while current:
            node = Node(current.data)

            if new_list.__head is None:
                new_list.__head = new_list.__tail = node
            else:
                node.next = new_list.__head
                new_list.__head.prev = node
                new_list.__head = node

            current = current.prev

        return new_list

    def sort_asc(self):
        current = self.__head

        while current:
            index = current.next

            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data

                index = index.next

            current = current.next

    def sort_desc(self):
        current = self.__head

        while current:
            index = current.next

            while index:
                if current.data < index.data:
                    current.data, index.data = index.data, current.data

                index = index.next

            current = current.next

    def display(self):
        current = self.__head
        output = ""

        while current:
            output += str(current.data) + " "
            current = current.next

        return output.strip()

    def display_reverse(self):
        current = self.__tail
        output = ""

        while current:
            output += str(current.data) + " "
            current = current.prev

        return output.strip()


# TESTING
d = Doubly()

d.add_first(3)
d.add_first(2)
d.add_first(1)
print("Add first:", d.display())

d.add_last(4)
print("Add last:", d.display())

d.add_before(0, 1)
print("Add before:", d.display())

d.add_after(5, 4)
print("Add after:", d.display())

d.del_first()
print("Delete first:", d.display())

d.del_last()
print("Delete last:", d.display())

d.del_given(3)
print("Delete given:", d.display())

print("Length:", d.length())
print("Total:", d.total())
print("Largest:", d.largest())
print("Smallest:", d.smallest())

print("Reversed copy:", d.reverse().display())

d.sort_asc()
print("Ascending:", d.display())

d.sort_desc()
print("Descending:", d.display())

print("Display backward:", d.display_reverse())
