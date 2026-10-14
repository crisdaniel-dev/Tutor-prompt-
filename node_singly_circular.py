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
