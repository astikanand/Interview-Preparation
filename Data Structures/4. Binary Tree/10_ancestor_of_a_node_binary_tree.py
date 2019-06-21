class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    

def print_ancestors(root, k):
    # If root is None return False.
    if root is None:
        return False
    
    # If root.val is given_node then return True.
    if root.val == k:
        return True
    
    # Print the root.data if any of root.left or root.right contains the given_node and return True.
    if(print_ancestors(root.left, k) or print_ancestors(root.right, k)):
        print(root.val, end=" ")
        return True
    
    # If given_node not in tree, return False
    return False
    
    
 

# Root
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left   = Node(4)
root.left.right  = Node(5)
root.left.left.left   = Node(7)

print("Ancestors of given_node k=7:")
print_ancestors(root, 7)
print()

print("Ancestors of given_node k=3:")
print_ancestors(root, 3)
print()