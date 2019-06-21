import sys
INT_MIN = -sys.maxsize-1

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


# Computes the number of nodes in tree
def size(root):
    if root is None:
        return 0
    else:
        return (1 + size(root.left) + size(root.right))


# Computes the height of tree
def height(root):
    if root is None:
        return 0
    else :
        return (1 + max(height(root.left), height(root.right)))


# Computes the number of nodes in tree
def maximum(root):
    if root is None:
        return INT_MIN
    else:
        return max(root.val, maximum(root.left), maximum(root.right))


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

print("Size of Tree: {}".format(size(root)))
print("Height of Tree: {}".format(height(root)))
print("Max of Tree: {}".format(maximum(root)))
