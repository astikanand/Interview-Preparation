class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 

def inorder_without_recursion(root):
    current = root 
    stack = []

    while(current is not None or len(stack) > 0):
        # Reach the left most Node of the current Node 
        while (current is not None):
            # Place pointer to a tree node on the stack before traversing the node's left subtree 
            stack.append(current)
            current = current.left 
        
        # Current must be NULL at this point
        current = stack.pop()
        print(current.val, end=" ")
         
        # We have visited the node and its left subtree. Now, it's right subtree's turn
        current = current.right 
    print()
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
inorder_without_recursion(root)
