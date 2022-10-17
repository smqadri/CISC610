from Binary_Node import BinaryNode


class LinkedHeap():
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    
    def find_node_to_insert(self):
        '''
        Find the node to insert the new node. 
        This find_node_to_insert will find the last node and the node where the new node will be inserted
        The last node is not neccearily the node where the new node will be inserted (it can be part of a full branch)
        Then we need to find the next node that does not have children yet. To do that we are doing a BFS search.
        '''
        last = self.root
        list = [last] # First list of nodes to check
        while True:
            if list[0] and not list[0].get_left():
                return last, list[0]

            new_list = [None] * (len(list) * 2)       # Second list of nodes to check
            i = 0
            for node in list:
                if not node:
                    return last, None
                left = node.get_left()
                if left is None:
                    return last, node
                new_list[i] = left
                i += 1
                last = left

                right = node.get_right()
                if right is None:
                    return last, node
                new_list[i] = right
                i += 1
                last = right

            list = new_list
    
    def _raw_insert(self, key, value):
        '''
        This raw_insert method will use the method find_node_to_insert to find the node where the new node will be inserted
        Still we are not doing the upheap operation. Just position the new node in the heap
        '''
        new_node = BinaryNode((key, value))
        self.size += 1

        if self.root is None:
            self.root = new_node
            return new_node

        _, node_to_insert = self.find_node_to_insert()

        if not node_to_insert.get_left():
            return self.link_left(node_to_insert, new_node)

        if not node_to_insert.get_right():
            return self.link_right(node_to_insert, new_node)

        self.size -= 1
        raise Exception("The Node already has two children")

    def insert(self, key, value):           # Insert a new node in the heap and move it up the heap until it is in the correct position
        node = self._raw_insert(key, value)
        self._upheap(node)
        return node

    def _upheap(self, node):            # Move the node up the heap until it is in the correct position
        '''
        Move the node up the heap until it is in the correct position
        While the node is not the root and the node is smaller than its parent, swap the node with its parent
        Swap the node with its parent until the node is in the correct position
        Move the node up the heap until it is in the correct position
        '''
        current = node
        #print(f"element current: {current.get_element()[0]}")
        while current:
            parent = current.get_parent()
            if parent is None:
                self.root = current
                return
            
            if parent.get_element()[0] > current.get_element()[0]:
                #print(f"element current parent: {current.get_parent().get_element()[0]}")
                #print(current.get_parent())
                self.swap_node_with_parent(current)

            current = parent

    def swap_node_with_parent(self, node):
        parent = node.get_parent()
        if not parent:
            return
        is_node_left = parent.get_left() == node
        #print(f"is node left: {parent.get_left() == node}")
        if is_node_left:
            self.swap_node_with_left_child(parent)
        else:
            self.swap_node_with_right_child(parent)

    def swap_node_with_left_child(self, node):
        left_child = node.get_left()
        if not left_child:
            return

        parent, is_left = self.unlink_parent(node)
        left = self.unlink_left(node)
        right = self.unlink_right(node)
        grand_left_child = self.unlink_left(left)
        grand_right_child = self.unlink_right(left)

        if not parent:
            self.root = left
        if is_left:
            self.link_left(parent, left)
        else:
            self.link_right(parent, left)
        self.link_right(left, right)
        self.link_left(left, node)
        self.link_right(node, grand_right_child)
        self.link_left(node, grand_left_child)


    def swap_node_with_right_child(self, node):
        right_child = node.get_right()
        if not right_child:
            return

        parent, is_left = self.unlink_parent(node)
        left = self.unlink_left(node)
        right = self.unlink_right(node)
        grand_left_child = self.unlink_left(right)
        grand_right_child = self.unlink_right(right)

        if not parent:
            self.root = right
        if is_left:
            self.link_left(parent, right)
        else:
            self.link_right(parent, right)
        self.link_right(right, node)
        self.link_left(right, left)
        self.link_right(node, grand_right_child)
        self.link_left(node, grand_left_child)
    
    def link_left(self, node, left):
        if not node:
            return
        node.set_left(left)
        if left:
            left.set_parent(node)
        return left

    def link_right(self, node, right):
        if not node:
            return
        node.set_right(right)
        if right:
            right.set_parent(node)
        return right

    def unlink_parent(self, node):
        parent = node.get_parent()
        if not parent:
            return None, None
        if parent.get_left() == node:
            parent.set_left(None)
            return node.set_parent(None), True
        elif parent.get_right() == node:
            parent.set_right(None)
            return node.set_parent(None), False
        return None, None

    def unlink_left(self, node):
        if not node:
            return None
        left = node.get_left()
        if left:
            node.set_left(None)
            left.set_parent(None)
        return left

    def unlink_right(self, node):
        if not node:
            return None
        right = node.get_right()
        if right:
            node.set_right(None)
            right.set_parent(None)
        return right

    def delete(self):
        '''
        Delete the root node and return the element
        Swap the data between the root and the last node
        - Remove the most recently added node from the heap
        - Restore the heap order via downheap operation
        Remove the most recently added node from the heap
        - Retain the data of the leaf node
        - Set the leaf node's parent to point to None
        - Set the appropriate child pointer of the leaf node's parent to None
        '''
        if self.size == 0:
            return

        old_root = self.root
        root_value = old_root.get_element()

        if self.size == 1:
            self.size -= 1
            self.root = None
            return root_value

        leaf, _ = self.find_node_to_insert()

        self.unlink_parent(leaf)
        
        root_left = self.unlink_left(old_root)
        root_right = self.unlink_right(old_root)

        self.link_left(leaf, root_left)
        self.link_right(leaf, root_right)

        self.size -= 1
        self.root = leaf

        self._downheap(leaf)
        return root_value
    
    def _downheap(self, node):
        '''
        Move the node down the heap until it is in the correct position
        Start with the root
        While the current node is not a leaf and the relationship between the current node and its children is not correct, 
        Swap the current node with its smallest child
        (i.e. The min key in a min heap, the max key in a max heap)
        Move the node down the heap until it is in the correct position        
        '''
        key = node.get_element()[0]
        while True:
            if not node.get_right():        # if no right child
                if not node.get_left():     # if no left child
                    break
                else:
                    key_left = node.get_left().get_element()[0]         # get left child key
                    if key > key_left:                                  # if key is greater than left child key
                        self.swap_node_with_left_child(node)
                    else:
                        break
            elif not node.get_left():
                key_right = node.get_right().get_element()[0]           # get right child key
                if key > key_right:                                     # if key is greater than right child key
                    self.swap_node_with_right_child(node)
                else:
                    break
            else:
                key_left = node.get_left().get_element()[0]
                key_right = node.get_right().get_element()[0]
                if key < key_left and key < key_right:            # Do nothing when the key of the node comply the min heap rule
                    break
                if key_left <= key_right:                       # which is the child with min key
                    if key > key_left:
                        self.swap_node_with_left_child(node)
                    else:
                        break
                else:
                    if key > key_right:
                        self.swap_node_with_right_child(node)
                    else:
                        break

    def print(self):
        if self.root is None:
            return
        level = [self.root]
        while len(level) > 0:
            next_level = []
            for node in level:
                print(node.get_element(), end=" ")
                if node.get_left() is not None:
                    next_level.append(node.get_left())
                if node.get_right() is not None:
                    next_level.append(node.get_right())
            print()
            level = next_level

    def peek(self):
        return self.root.get_element()

    def is_empty(self):
        return self.size == 0

