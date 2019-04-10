class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Computes the number of nodes in tree
def size(root):
    if root is None:
        return 0
    else:
        return (size(root.left)+ 1 + size(root.right))
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
 
print ("Size of the tree is %d" %(size(root)))