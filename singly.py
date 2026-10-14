from node_singly_circular import Node


class Singly:

    def __init__(self):
        self.__head = None

    def add_first(self, data):
        node = Node(data)
        node.next = self.__head
        self.__head = node

    def add_last(self, data):
        node = Node(data)
        if not self.__head:
            self.__head = node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = node

    def front(self):
        assert self.__head, "List is empty"
        return self.__head.data

    def rear(self):
        assert self.__head, "List is empty"
        current = self.__head
        while current.next:
            current = current.next
        return current.data

    def add_before(self, target, data):
        assert self.__head, "List is empty"
        if self.__head.data == target:
            self.add_first(data)
            return
        current = self.__head
        pre_current = None
        while current and current.data != target:
            pre_current = current
            current = current.next
        assert current, "Target not found"
        node = Node(data)
        node.next = current
        pre_current.next = node

    def add_after(self, target, data):
        assert self.__head, "List is empty"
        current = self.__head
        while current and current.data != target:
            current = current.next
        assert current, "Target not found"
        node = Node(data)
        node.next = current.next
        current.next = node

    def del_first(self):
        assert self.__head, "List is empty"
        self.__head = self.__head.next

    def del_last(self):
        assert self.__head, "List is empty"
        if not self.__head.next:
            self.__head = None
            return
        current = self.__head
        pre_current = None
        while current.next:
            pre_current = current
            current = current.next
        pre_current.next = None

    def del_given(self, target):         # delete a specific node by its value
        assert self.__head, "List is empty"
        if self.__head.data == target:   # target is the head
            self.__head = self.__head.next
            return
        current = self.__head
        pre_current = None
        while current and current.data != target:
            pre_current = current
            current = current.next
        assert current, "Target not found"
        pre_current.next = current.next  # the node behind skips the target

    def display(self):
        assert self.__head, "List is empty"
        current = self.__head
        output = ""
        while current:
            output += str(current.data) + " "
            current = current.next
        return output.strip()

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
        new_list = Singly()             # an object created inside the class
        current = self.__head
        while current:
            new_list.add_first(current.data)    # add_first flips the order
            current = current.next
        return new_list

    def reverse_in_place(self):         # reverses THIS list (no new list)
        previous = None
        current = self.__head
        while current:
            following = current.next    # 1. remember the next node
            current.next = previous     # 2. turn the arrow backwards
            previous = current          # 3. move previous forward
            current = following         # 4. move current forward
        self.__head = previous          # previous ends on the old last node


s = Singly()
s.add_first(4)
s.add_first(3)
s.add_first(2)
s.add_last(9)
print(s.display())                      # 2 3 4 9
print(s.length())                       # 4
print(s.total())                        # 18
print(s.largest(), s.smallest())        # 9 2
r = s.reverse()
print(r.display())                      # 9 4 3 2
print(s.display())                      # 2 3 4 9  (the original did not change)
s.reverse_in_place()
print(s.display())                      # 9 4 3 2
s.del_given(3)
print(s.display())                      # 9 4 2
