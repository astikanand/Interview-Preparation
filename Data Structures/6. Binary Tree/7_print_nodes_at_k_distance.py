class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    

def print_nodes_at_k_distance(root, k):
    if root is None:
        return
    
    if k==0:
        print(root.val, end=" ")
    else:
        print_nodes_at_k_distance(root.left, k-1)
        print_nodes_at_k_distance(root.right, k-1)

 

# Root
root = Node(50)

# 1st Level
root.left      = Node(17)
root.right     = Node(72)

# 2nd Level
root.left.left   = Node(12)
root.left.right  = Node(23)
root.right.left  = Node(54)
root.right.right = Node(76)

# 3rd Level
root.left.left.left   = Node(9)
root.left.left.right  = Node(14)
root.left.right.right = Node(19)
root.right.left.right = Node(67)

print("Nodes at distance of k=2:")
print_nodes_at_k_distance(root, 2)
print()
