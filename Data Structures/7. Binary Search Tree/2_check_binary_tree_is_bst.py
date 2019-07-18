import sys
INT_MIN = -sys.maxsize-1
INT_MAX = sys.maxsize

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_bst(root): 
    return (is_bst_util(root, INT_MIN, INT_MAX)) 
  

def is_bst_util(root, min_val, max_val): 
    # An empty tree is BST 
    if root is None: 
        return True
  
    # If current root's val is either less than min_val allowed or greater than max_val allowed return False.
    if root.val < min_val or root.val > max_val: 
        return False
  
    # Check the subtrees recursively tightening the min or max constraint 
    return (is_bst_util(root.left, min_val, root.val-1) and is_bst_util(root.right, root.val+1, max_val)) 


def print_tree(root):
    if(root):
        print_tree(root.left)
        print(root.val, end=" ")
        print_tree(root.right)
   


root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3)
print("Binary Tree:")
print_tree(root)
print()
print("Is this binary Tree a BST ? : {}".format(is_bst(root)))

root = Node(3)
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(4)
print("\nAnother Binary Tree:")
print_tree(root)
print()
print("Is this binary Tree a BST ? : {}".format(is_bst(root)))