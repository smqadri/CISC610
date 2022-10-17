from LinkedHeap import LinkedHeap

class PriorityQueue:

    def __init__(self):
        self.linkedheap = LinkedHeap()

    def add(self, key, value):
        self.linkedheap.insert(key, value)

    def remove(self):
        return self.linkedheap.delete()

    def min(self):
        return self.linkedheap.peek()
    
    def is_empty(self):
        return self.linkedheap.is_empty()
    
    def len(self):
        return self.linkedheap.size
