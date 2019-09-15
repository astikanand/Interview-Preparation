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
root = Node(13)

# 1st Level
root.left      = Node(7)
root.right     = Node(2)

# 2nd Level
root.left.left   = Node(19)
root.left.right  = Node(25)

# 3rd Level
root.left.left.left   = Node(11)
root.left.left.right  = Node(28)
root.left.right.right = Node(5)

# 4th Level
root.left.left.right.left = Node(35)
root.left.right.right.left = Node(7)
root.left.right.right.right = Node(9)

# 5th Level
root.left.left.right.left.right = Node(26)
root.left.right.right.right.left = Node(17)


print("Diameter of Tree: {}".format(diameter(root)))