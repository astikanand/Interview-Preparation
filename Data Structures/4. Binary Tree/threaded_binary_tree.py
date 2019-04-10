# A threaded binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
        self.rightThread = False
 
# Iterative function for inorder tree traversal
def inOrder(root):  
    # Set current to root of binary tree
    current = root 
    s = [] # initialze stack

    while(current is not None or len(s) > 0):

        # Reach the left most Node of the current Node 
        while (current is not None):
            # place pointer to a tree node on the stack before traversing the node's left subtree 
            s.append(current)
            current = current.left 
        
        # Current must be NULL at this point
        current = s.pop()
        print(current.data, end=" ")
         
        # We have visited the node and its left subtree. Now, it's right subtree's turn
        current = current.right 
            
     
 
# Driver program to test above function
 
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
inOrder(root)