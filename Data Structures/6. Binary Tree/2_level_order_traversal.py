class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def level_order_traversal(root):
    # (1) If root is None, then return.
    if root is None:
        return
    
    # (2) Create an empty queue.
    queue = []

    # (3) Enqueue root to queue.
    queue.append(root)

    # (4) while queue is not empty.
    while(queue):
        # Dequeue the temp_node from queue.
        temp_node = queue.pop(0)

        # Print temp_node.val
        print(temp_node.val, end=" ")

        # If temp_node's left exists: enqueue left to queue.
        if (temp_node.left):
            queue.append(temp_node.left)
        
        # And if right exists: enqueue right also to queue.
        if (temp_node.right):
            queue.append(temp_node.right)

    
    


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

print("Level Order Traversal:")
level_order_traversal(root)
print()