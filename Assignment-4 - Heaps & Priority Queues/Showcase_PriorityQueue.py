from PriorityQueue import PriorityQueue

pq = PriorityQueue()



print('=========================')
print("Adding 11, 7, 8, 6, 5, 9, 4 to the PriorityQueue")
pq.add(11, 0)
pq.add(7, 0)
pq.add(8, 0)
pq.add(6, 0)
pq.add(5, 0)
pq.add(9, 0)
pq.add(4, 0)
pq.linkedheap.print()
print('=========================')
print("Dequeue three highest priority items:")
print(pq.remove())
print(pq.remove())
print(pq.remove())

print('=========================')
print("Priority Queue after removing the three highest priority items:")
pq.linkedheap.print()
print('=========================')

