import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize -1


class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Computes the number of nodes in tree
def maximum(root):
    if root is None:
        return INT_MIN
    else:
        return max(root.data, maximum(root.left), maximum(root.right))
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
 
print ("Maximum element in the tree is %d" %(maximum(root)))