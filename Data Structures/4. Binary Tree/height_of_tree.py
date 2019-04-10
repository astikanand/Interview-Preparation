class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

# Computes the height of tree
def height(node):
    if node is None:
        return 0
    else :
        return 1+max(height(node.left), height(node.right))


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
 
print ("Height of the tree is %d" %(height(root)))