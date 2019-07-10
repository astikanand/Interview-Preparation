from collections import defaultdict

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def get_vertical_order(root, level, my_hash): 
    if root is None: 
        return
    
    # Put the root in hash with level
    my_hash[level].append(root.val)

    # Decrease the level while going in left subtree
    get_vertical_order(root.left, level-1, my_hash)

    # Increase the level while going in right subtree
    get_vertical_order(root.right, level+1, my_hash) 
  

def print_vertical_order(root): 
    # Hash to store vertical order
    my_hash = defaultdict(list)
    level = 0 
    get_vertical_order(root, level, my_hash) 

    for key, values in sorted(my_hash.items()):
        print("[{}] :-----> ".format(key), end = "")
        for v in values:
            print(v, end=" ")
        print()



root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 
print ("Vertical order traversal:")
print_vertical_order(root)
