from node_doubly import Node


class CircularDoubly:

    def __init__(self):
        self.__head = self.__tail = None

    def add_first(self, data):
        node = Node(data)

        if self.__head:
            node.next = self.__head           # new node -> old head
            node.prev = self.__tail           # new node <- tail
            self.__head.prev = node           # old head <- new node
            self.__tail.next = node           # tail -> new node
            self.__head = node                # head moves to the new node
        else:
            self.__head = self.__tail = node
            node.next = node.prev = node      # points at itself both ways

    def add_last(self, data):
        node = Node(data)

        if self.__head:
            node.prev = self.__tail           # new node <- old tail
            node.next = self.__head           # new node -> head
            self.__tail.next = node           # old tail -> new node
            self.__head.prev = node           # head <- new node
            self.__tail = node                # tail moves to the new node
        else:
            self.__head = self.__tail = node
            node.next = node.prev = node

    def add_after(self, data, key):
        assert self.__head, "List is empty"
        current = self.__head

        while True:
            if current.data == key:
                # key is the tail: same as add_last
                if current is self.__tail:
                    self.add_last(data)
                    return

                node = Node(data)
                node.prev = current           # new node <- key node
                node.next = current.next      # new node -> node after the key
                current.next.prev = node      # node after the key <- new node
                current.next = node           # key node -> new node
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
                # key is the head: same as add_first
                if current is self.__head:
                    self.add_first(data)
                    return

                node = Node(data)
                node.next = current           # new node -> key node
                node.prev = current.prev      # new node <- node before the key
                current.prev.next = node      # node before the key -> new node
                current.prev = node           # key node <- new node
                return

            current = current.next

            if current is self.__head:
                break

        raise ValueError("Key not found")

    def del_first(self):
        assert self.__head, "List is empty"
        data = self.__head.data

        if self.__head is self.__tail:        # one node left
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = self.__tail    # new head <- tail
            self.__tail.next = self.__head    # tail -> new head

        return data

    def del_last(self):
        assert self.__head, "List is empty"
        data = self.__tail.data

        if self.__head is self.__tail:        # one node left
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = self.__head    # new tail -> head
            self.__head.prev = self.__tail    # head <- new tail

        return data

    def del_given(self, key):
        assert self.__head, "List is empty"
        current = self.__head

        while True:
            if current.data == key:
                if current is self.__head:
                    return self.del_first()

                if current is self.__tail:
                    return self.del_last()

                current.prev.next = current.next    # node before -> node after
                current.next.prev = current.prev    # node after <- node before
                return current.data

            current = current.next

            if current is self.__head:
                break

        raise ValueError("Key not found")

    def is_circular(self):
        if not self.__head or not self.__tail:
            return False

        return self.__tail.next is self.__head and self.__head.prev is self.__tail

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

    def display_reverse(self):
        assert self.__head, "List is empty"
        current = self.__tail
        output = ""

        while True:
            output += str(current.data) + " "
            current = current.prev
            if current is self.__tail:
                break

        return output.strip()

    def head(self):
        assert self.__head, "List is empty"
        return self.__head.data

    def tail(self):
        assert self.__head, "List is empty"
        return self.__tail.data

    # ---------- the extra problems ----------

    def length(self):
        if not self.__head:
            return 0
        count = 0                       # start at 0
        current = self.__head
        while True:
            count += 1                  # one more node
            current = current.next
            if current is self.__head:  # back at the head: stop
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
            if current is self.__head:
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
            if current is self.__head:
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
            if current is self.__head:
                break
        return smallest

    def reverse(self):                  # returns a NEW reversed list
        new_list = CircularDoubly()     # an object created inside the class
        if not self.__head:
            return new_list
        current = self.__head
        while True:
            new_list.add_first(current.data)    # add_first flips the order
            current = current.next
            if current is self.__head:
                break
        return new_list

    def reverse_in_place(self):         # reverses THIS list (no new list)
        if not self.__head:
            return
        current = self.__head
        while True:
            following = current.next                            # remember the next node
            current.next, current.prev = current.prev, current.next   # swap its two links
            current = following
            if current is self.__head:
                break
        self.__head, self.__tail = self.__tail, self.__head     # swap the ends


cd = CircularDoubly()
for n in (7, 8, 9, 1, 2):
    cd.add_first(n)
print(cd.display())                 # 2 1 9 8 7
print(cd.display_reverse())         # 7 8 9 1 2
cd.add_last(5)
cd.add_after(6, 7)
cd.add_before(0, 2)
print(cd.display())                 # 0 2 1 9 8 7 6 5
cd.del_first()
cd.del_last()
cd.del_given(9)
print(cd.display())                 # 2 1 8 7 6
print(cd.display_reverse())         # 6 7 8 1 2
print(cd.head(), cd.tail())         # 2 6
print(cd.is_circular())             # True
print(cd.length())                  # 5
print(cd.total())                   # 24
print(cd.largest(), cd.smallest())  # 8 1
print(cd.reverse().display())       # 6 7 8 1 2
cd.reverse_in_place()
print(cd.display())                 # 6 7 8 1 2
