
import bintree_tree            # for binary tree traversal
import tree_traversal           # for tree traversal
import breadth_first_traverse   # for breadth first traversal



if __name__ == '__main__':
    tree = bintree_tree.Tree()                      # create a binary tree
    with open('random_numbers.csv','r') as file:    # open the file
        data = file.read()                          # read the file
    for i in data.split(","):                       # split the data
        tree.insert(i)                              # insert the data into the tree
    num_leaf = breadth_first_traverse.breadth_first_traversal(tree.root_node)   # count number of leaf nodes
    height = tree_traversal.inorder(tree.root_node)                    # find height of tree
    print("number of leaves in the tree is {}".format(num_leaf))
    print("height of tree is {}".format(height))