from LinkedHeap import LinkedHeap

lh = LinkedHeap()


lh.insert(11, 0)
lh.insert(7, 0)
lh.insert(8, 0)
lh.insert(6, 0)
lh.insert(5, 0)
lh.insert(9, 0)
lh.insert(4, 0)



print('=========================')
lh.print()
print("\nSize of the LinkedHeap is: ", lh.size)
print('=========================')

print("Peek into the LinkedHeap:", lh.peek())


print('=========================')
print('Calling the Delete subroutine.')
lh.delete()
print('\n=========================')
lh.print()
print('=========================')
print("\nSize of the LinkedHeap is: ", lh.size)
print('=========================')
print("\nCheck if LinkedHeap is empty:", lh.is_empty())
print('\nCalling the Delete subroutine six more times.\n')
print('\n======== Delete 6=================')
lh.delete()
lh.print()
print('\n======== Delete 5=================')
lh.delete()
lh.print()
print('\n======== Delete 4=================')
lh.delete()
lh.print()
print('\n======== Delete 3=================')
lh.delete()
lh.print()
print('\n======== Delete 2=================')
lh.delete()
lh.print()
print('\n======== Delete 1=================')
lh.delete()
lh.print()
print('\n=========================')
print("\nCheck if LinkedHeap is empty:", lh.is_empty())