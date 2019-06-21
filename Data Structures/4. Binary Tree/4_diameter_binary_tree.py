import sys
INT_MIN = -sys.maxsize-1

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def height(root, max_diam):
    if root is None:
        return 0
    else :
        # Get the height of left and right nodes of the current_node
        left_height = height(root.left, max_diam)
        right_height = height(root.right, max_diam)

        # Get the diameter at current_node = 1 + left_height + right_height
        # Update the max_diam[0] if current_diam > max_diam[0]
        current_diam = 1 + left_height + right_height
        max_diam[0] = max(max_diam[0], current_diam)

        # return the height of the current_node
        return (1 + max(left_height, right_height))


def diameter(root):
    if root is None:
        return 0
    
    max_diam = [INT_MIN]    # This will store the final answer
    height(root, max_diam)
    return max_diam[0]


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

print("Diameter of Tree: {}".format(diameter(root)))