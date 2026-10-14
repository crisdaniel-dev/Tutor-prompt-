from node_singly_circular import Node


class Circular:

    def __init__(self):
        self.__head = self.__tail = None

    def add_first(self, data):
        node = Node(data)

        if self.__head:
            node.next = self.__head          # node -> old head
            self.__head = node               # head moves to the node
            self.__tail.next = self.__head   # tail -> new head
        else:
            self.__head = self.__tail = node
            self.__tail.next = self.__head   # points at itself

    def add_last(self, data):
        node = Node(data)

        if self.__head:
            self.__tail.next = node
            self.__tail = node
        else:
            self.__head = self.__tail = node

        self.__tail.next = self.__head

    def add_after(self, data, key):
        assert self.__head, "List is empty"
        node = Node(data)
        current = self.__head

        while True:
            if current.data == key:
                node.next = current.next
                current.next = node

                if current == self.__tail:
                    self.__tail = node

                return

            current = current.next

            if current == self.__head:
                break

        raise ValueError("Key not found")

    def add_before(self, data, key):
        assert self.__head, "List is empty"

        # key is the head: same as add_first
        if self.__head.data == key:
            self.add_first(data)
            return

        node = Node(data)
        pre_current = self.__head
        current = self.__head.next

        while current != self.__head:
            if current.data == key:
                node.next = current          # new node -> key node
                pre_current.next = node      # node behind -> new node
                return

            pre_current = current
            current = current.next

        raise ValueError("Key not found")

    def is_circular(self):
        if not self.__head or not self.__tail:
            return False

        return self.__tail.next is self.__head

    def del_first(self):
        assert self.__head, "List is empty"
        data = self.__head.data

        if self.__head is self.__tail:       # one node left
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__tail.next = self.__head

        return data

    def del_last(self):
        assert self.__head, "List is empty"
        data = self.__tail.data

        if self.__head is self.__tail:       # one node left
            self.__head = self.__tail = None
            return data

        current = self.__head
        while current.next is not self.__tail:    # stop on the node before the tail
            current = current.next

        current.next = self.__head
        self.__tail = current

        return data

    def del_given(self, key):
        assert self.__head, "List is empty"

        # key is the head: same as del_first
        if self.__head.data == key:
            return self.del_first()

        pre_current = self.__head
        current = self.__head.next

        while current != self.__head:
            if current.data == key:
                pre_current.next = current.next

                if current is self.__tail:
                    self.__tail = pre_current

                return current.data

            pre_current = current
            current = current.next

        raise ValueError("Key not found")

    def display(self):
        assert self.__head, "List is empty"
        current = self.__head
        output = ""

        while True:
            output += str(current.data) + " "
            current = current.next
            if current == self.__head:
                break

        return output.strip()

    def tail(self):
        # get the value of the tail
        assert self.__head, "List is empty"
        return self.__tail.data

    def head(self):
        # get the value of the head
        assert self.__head, "List is empty"
        return self.__head.data

    # ---------- the extra problems ----------

    def length(self):
        if not self.__head:
            return 0
        count = 0                       # start at 0
        current = self.__head
        while True:
            count += 1                  # one more node
            current = current.next
            if current == self.__head:  # back at the head: stop
                break
        return count

    def total(self):                    # sum of all values
        if not self.__head:
            return 0
        total = 0                       # start at 0
        current = self.__head
        while True:
            total += current.data       # add this node's value
            current = current.next
            if current == self.__head:
                break
        return total

    def largest(self):
        assert self.__head, "List is empty"
        current = self.__head
        largest = current.data          # start with the FIRST value, not 0
        while True:
            if current.data > largest:
                largest = current.data
            current = current.next
            if current == self.__head:
                break
        return largest

    def smallest(self):
        assert self.__head, "List is empty"
        current = self.__head
        smallest = current.data         # start with the FIRST value, not 0
        while True:
            if current.data < smallest:
                smallest = current.data
            current = current.next
            if current == self.__head:
                break
        return smallest

    def reverse(self):                  # returns a NEW reversed list
        new_list = Circular()           # an object created inside the class
        if not self.__head:
            return new_list
        current = self.__head
        while True:
            new_list.add_first(current.data)    # add_first flips the order
            current = current.next
            if current == self.__head:
                break
        return new_list

    def reverse_in_place(self):         # reverses THIS list (no new list)
        if not self.__head:
            return
        previous = self.__tail
        current = self.__head
        while True:
            following = current.next    # 1. remember the next node
            current.next = previous     # 2. turn the arrow backwards
            previous = current          # 3. move previous forward
            current = following         # 4. move current forward
            if current == self.__head:
                break
        self.__head, self.__tail = self.__tail, self.__head   # swap the ends



c = Circular()
for n in (7, 8, 9, 1, 2):
    c.add_first(n)
print(c.display())                 # 2 1 9 8 7
print(c.head(), c.tail())          # 2 7
c.add_last(5)
print(c.display())                 # 2 1 9 8 7 5
c.add_after(6, 7)
print(c.display())                 # 2 1 9 8 7 6 5
c.add_before(0, 2)
print(c.display())                 # 0 2 1 9 8 7 6 5
print(c.is_circular())             # True
c.del_first()
c.del_last()
c.del_given(9)
print(c.display())                 # 2 1 8 7 6

print(c.length())                  # 5
print(c.total())                   # 24
print(c.largest(), c.smallest())   # 8 1
print(c.reverse().display())       # 6 7 8 1 2
c.reverse_in_place()
print(c.display())                 # 6 7 8 1 2
