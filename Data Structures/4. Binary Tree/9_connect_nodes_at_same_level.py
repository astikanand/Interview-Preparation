class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nextright = None
        



def connect_nodes_at_same_level(root):
    # (1) If root is None, then return.
    if root is None:
        return
    
    # (2) Create an empty queue.
    queue = []

    # (3) Enqueue root to queue.
    queue.append(root)

    # (4) While queue is not empty.
    while(queue):
        # Get the current_count.
        current_count = len(queue)

        # Dequeue all the nodes instead of one. So, while current_count > 0.
        while(current_count > 0):
            # Dequeue the temp_node from queue.
            temp_node = queue.pop(0)

            print("{}--->".format(temp_node.val), end="")
            # Set the next_right and consider that at every level
            # the last element will not point to any other node as the front will be empty.
            if(current_count > 1):
                temp_node.nextright = queue[0]
            else:
                temp_node.nextright = None
                print("None")

            # If temp_node's left exists: enqueue left to queue.
            if (temp_node.left):
                queue.append(temp_node.left)
        
            # And if right exists: enqueue right also to queue.
            if (temp_node.right):
                queue.append(temp_node.right)
            
            current_count -= 1
    



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

# Call Function
connect_nodes_at_same_level(root)
