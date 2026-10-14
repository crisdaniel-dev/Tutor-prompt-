# REFERENCE CODE (source of truth for my style)

Fully tested code for all four list types. Test lines sit at the bottom of each file, without `if __name__`. In my exam the Node file is `node.py` and the list file starts with `from node import Node`. Here the import names differ only so both Node versions fit in one folder.

Argument order: singly `add_after(target, data)` and `add_before(target, data)`. Circular, doubly and circular doubly use `(data, key)`.

## node_singly_circular.py (Node for singly and circular)

```python
class Node:

    def __init__(self, data):
        self.data, self.next = data, None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int) or isinstance(data, bool):
            raise ValueError("Data must be a whole integer")

        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next
```

## node_doubly.py (Node for doubly and circular doubly, adds `prev`)

```python
class Node:

    def __init__(self, data):
        self.data, self.next, self.prev = data, None, None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int) or isinstance(data, bool):
            raise ValueError("Data must be a whole integer")

        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev
```

## singly.py (Singly (head only))

```python
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
```

## circular.py (Circular singly (head and tail))

```python
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
```

## doubly.py (Doubly (head and tail))

```python
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
```

## circular_doubly.py (Circular doubly (head and tail))

```python
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
```
