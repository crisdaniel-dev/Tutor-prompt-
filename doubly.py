from node_doubly import Node


class Doubly:

    def __init__(self):
        self.__head = self.__tail = None

    def add_first(self, data):
        node = Node(data)

        if self.__head:
            node.next = self.__head       # new node -> old head
            self.__head.prev = node       # old head <- new node
            self.__head = node            # head moves to the new node
        else:
            self.__head = self.__tail = node

    def add_last(self, data):
        node = Node(data)

        if self.__head:
            node.prev = self.__tail       # new node <- old tail
            self.__tail.next = node       # old tail -> new node
            self.__tail = node            # tail moves to the new node
        else:
            self.__head = self.__tail = node

    def add_after(self, data, key):
        assert self.__head, "List is empty"

        current = self.__head
        while current and current.data != key:
            current = current.next

        if not current:
            raise ValueError("Key not found")

        # key is the tail: same as add_last
        if current is self.__tail:
            self.add_last(data)
            return

        node = Node(data)
        node.prev = current               # new node <- key node
        node.next = current.next          # new node -> node after the key
        current.next.prev = node          # node after the key <- new node
        current.next = node               # key node -> new node

    def add_before(self, data, key):
        assert self.__head, "List is empty"

        current = self.__head
        while current and current.data != key:
            current = current.next

        if not current:
            raise ValueError("Key not found")

        # key is the head: same as add_first
        if current is self.__head:
            self.add_first(data)
            return

        node = Node(data)
        node.next = current               # new node -> key node
        node.prev = current.prev          # new node <- node before the key
        current.prev.next = node          # node before the key -> new node
        current.prev = node               # key node <- new node

    def del_first(self):
        assert self.__head, "List is empty"
        data = self.__head.data

        if self.__head is self.__tail:    # one node left
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None

        return data

    def del_last(self):
        assert self.__head, "List is empty"
        data = self.__tail.data

        if self.__head is self.__tail:    # one node left
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None

        return data

    def del_given(self, key):
        assert self.__head, "List is empty"

        current = self.__head
        while current and current.data != key:
            current = current.next

        if not current:
            raise ValueError("Key not found")

        if current is self.__head:
            return self.del_first()

        if current is self.__tail:
            return self.del_last()

        current.prev.next = current.next  # node before -> node after
        current.next.prev = current.prev  # node after <- node before

        return current.data

    def display(self):
        assert self.__head, "List is empty"
        current = self.__head
        output = ""

        while current:
            output += str(current.data) + " "
            current = current.next

        return output.strip()

    def display_reverse(self):
        assert self.__head, "List is empty"
        current = self.__tail
        output = ""

        while current:
            output += str(current.data) + " "
            current = current.prev

        return output.strip()

    def head(self):
        assert self.__head, "List is empty"
        return self.__head.data

    def tail(self):
        assert self.__head, "List is empty"
        return self.__tail.data

    # ---------- the extra problems ----------

    def length(self):
        count = 0                       # start at 0
        current = self.__head
        while current:
            count += 1                  # one more node
            current = current.next
        return count

    def total(self):                    # sum of all values
        total = 0                       # start at 0
        current = self.__head
        while current:
            total += current.data       # add this node's value
            current = current.next
        return total

    def largest(self):
        assert self.__head, "List is empty"
        current = self.__head
        largest = current.data          # start with the FIRST value, not 0
        while current:
            if current.data > largest:
                largest = current.data
            current = current.next
        return largest

    def smallest(self):
        assert self.__head, "List is empty"
        current = self.__head
        smallest = current.data         # start with the FIRST value, not 0
        while current:
            if current.data < smallest:
                smallest = current.data
            current = current.next
        return smallest

    def reverse(self):                  # returns a NEW reversed list
        new_list = Doubly()             # an object created inside the class
        current = self.__head
        while current:
            new_list.add_first(current.data)    # add_first flips the order
            current = current.next
        return new_list

    def reverse_in_place(self):         # reverses THIS list (no new list)
        current = self.__head
        while current:
            following = current.next                            # remember the next node
            current.next, current.prev = current.prev, current.next   # swap its two links
            current = following
        self.__head, self.__tail = self.__tail, self.__head     # swap the ends



d = Doubly()
for n in (7, 8, 9, 1, 2):
    d.add_first(n)
print(d.display())                 # 2 1 9 8 7
print(d.display_reverse())         # 7 8 9 1 2
d.add_last(5)
d.add_after(6, 7)
d.add_before(0, 2)
print(d.display())                 # 0 2 1 9 8 7 6 5
d.del_first()
d.del_last()
d.del_given(9)
print(d.display())                 # 2 1 8 7 6
print(d.display_reverse())         # 6 7 8 1 2
print(d.head(), d.tail())          # 2 6

print(d.length())                  # 5
print(d.total())                   # 24
print(d.largest(), d.smallest())   # 8 1
print(d.reverse().display())       # 6 7 8 1 2
d.reverse_in_place()
print(d.display())                 # 6 7 8 1 2
