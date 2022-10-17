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

height = 0
max_height = 0
number_leaves = 0


current = n1 
'''
while current: 
        print(current.data) 
        current = current.left_child 

print("\n" )
'''
def inorder(root_node):                                         
        current = root_node                                     
        if current is None:                                     
            return                                              
        inorder(current.left_child)                             
        print(current.data)                                     
        inorder(current.right_child)                            
'''
def preorder(root_node): 
        current = root_node 
        if current is None: 
            return 
        print(current.data) 
        preorder(current.left_child) 
        preorder(current.right_child) 
'''

def preorder(root_node):                                                    # preorder tree traversal
        current = root_node                                                 # start from root node
        global number_leaves, height, max_height                            # declare global variables
        if current is None:                                                 # if current node is None    
            return
        if (current.left_child != None or current.right_child != None):     # if current node has children
            height += 1                                                     # increment height                       
            max_height = max(height, max_height)                            # update max height
        if (current.left_child is None and current.right_child is None):    # if current node is a leaf
            number_leaves += 1                                              # increment number of leaves
            height = 0                                                      # reset height                
        preorder(current.left_child)                                        # go to left child
        preorder(current.right_child)                                       # go to right child

def postorder(root_node):                                                   
        current = root_node                                                 
        if current is None:                                                
            return 
        postorder(current.left_child)                                      
        postorder(current.right_child)                                      
        print(current.data)                                                



'''
inorder( n1)
print("\n" )
preorder( n1)
print("\n" )
postorder(n1)
'''