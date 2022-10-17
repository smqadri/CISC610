class ArrayHeap:

    #----------------------------------------------------------

    class _Item:
        
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def get_key(self):
            return self._key
        
        def get_value(self):
            return self._value

        def __lt__(self, other):
            return self.get_key() < other.get_key()

        def __gt__(self, other):
            return self.get_key() > other.get_key()

        def __str__(self):
            return "(" + str(self.get_key()) + ", " + str(self.get_value()) + ")"

        def __repr__(self):
            return "(" + str(self.get_key()) + ", " + str(self.get_value()) + ")"

    #----------------HEAP HELPER METHODS-------------------------

    def _left_child(self, index):
        return (index * 2) + 1

    def _right_child(self, index):
        return (index * 2) + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _has_left(self, index):
        return self._left_child(index) < len(self._data)

    def _has_right(self, index):
        return self._right_child(index) < len(self._data)

    def _has_parent(self, index):
        return index > 0

    def _swap(self, index1, index2):
        self._data[index1], self._data[index2] = self._data[index2], self._data[index1]
        #temp = self._data[index1]
        #self._data[index1] = self._data[index2]
        #self._data[index2] = temp

    def _upheap(self, index):
        parent = self._parent(index)
        #if self._has_parent(index) and self._data[index].get_key() < self._data[parent].get_key():
        if self._has_parent(index) and self._data[index] < self._data[parent]:
            self._swap(index, parent)
            self._upheap(parent)

    def _downheap(self, index):
        if self._has_left(index):
            min_index = self._left_child(index)
            right_index = self._right_child(index)

            #if self._has_right(index) and self._data[right_index].get_key() < self._data[min_index].get_key():
            if self._has_right(index) and self._data[right_index] < self._data[min_index]:
                min_index = right_index

            #if self._data[min_index].get_key() < self._data[index].get_key():
            if self._data[min_index] < self._data[index]:
                self._swap(index, min_index)
                self._downheap(min_index)

    #----------------PRIORITY QUEUE METHODS----------------------

    def __init__(self):
        self._data = []

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self) - 1)

    def remove_min(self):
        old_min = self.min()
        self._swap(0, len(self) - 1)
        del(self._data[len(self) - 1])
        self._downheap(0)
        return old_min

    def min(self):
        return (self._data[0].get_key(), self._data[0].get_value())

    def is_empty(self):
        #return len(self._data) == 0
        return len(self) == 0

    def __len__(self):
        return len(self._data)
