from collections import deque 

class Node: 
        def __init__(self, data): 
            self.data = data 
            self.right_child = None 
            self.left_child = None 

n1 = Node("root node")  
n2 = Node("left child node") 
n3 = Node("right child node") 
n4 = Node("left grandchild node") 
n1.left_child = n2 
n1.right_child = n3 
n2.left_child = n4 

def breadth_first_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])
    num_leaf = 0                            # set number of leaf nodes = 0
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node)
        if node.left_child:
            traversal_queue.append(node.left_child)
        if node.right_child:
            traversal_queue.append(node.right_child)
        if not node.left_child and not node.right_child:        # if node is a leaf node
            num_leaf += 1                                       # increment number of leaf nodes
    return num_leaf                                             # return number of leaf nodes



#print(breadth_first_traversal(n1))