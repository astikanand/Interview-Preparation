class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def max_width_binary_tree(root):
    # (1) If root is None, then return 0.
    if root is None:
        return 0
    
    # (2) Create an empty queue and max_width=0.
    queue = []
    max_width = 0

    # (3) Enqueue root to queue.
    queue.append(root)

    # (4) While queue is not empty.
    while(queue):
        # Get the current_count and update max_width if it is greater.
        current_count = len(queue)
        max_width = max(max_width, current_count)

        # Dequeue all the nodes instead of one. So, while current_count > 0.
        while(current_count > 0):
            # Dequeue the temp_node from queue.
            temp_node = queue.pop(0)

            # If temp_node's left exists: enqueue left to queue.
            if (temp_node.left):
                queue.append(temp_node.left)
        
            # And if right exists: enqueue right also to queue.
            if (temp_node.right):
                queue.append(temp_node.right)
            
            current_count -= 1
    
    return max_width

    
    


# Root
root = Node(1)

# 1st Level
root.left      = Node(2)
root.right     = Node(3)

# 2nd Level
root.left.left   = Node(4)
root.left.right  = Node(5)
root.right.right = Node(8)

# 3rd Level
root.right.right.left  = Node(6)
root.right.right.right = Node(7)

print("Maximum Width = {}".format(max_width_binary_tree(root)))