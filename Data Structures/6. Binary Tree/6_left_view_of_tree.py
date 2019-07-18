class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def left_view_binary_tree(root):
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

        # Flag to know if first element in this level is printed.
        printed = False

        # Dequeue all the nodes instead of one. So, while current_count > 0.
        while(current_count > 0):
            # Dequeue the temp_node from queue.
            temp_node = queue.pop(0)

            # Print the first element in this level if it is not printed.
            if(not printed):
                print(temp_node.val, end=" ")
                printed = True

            # If temp_node's left exists: enqueue left to queue.
            if (temp_node.left):
                queue.append(temp_node.left)
        
            # And if right exists: enqueue right also to queue.
            if (temp_node.right):
                queue.append(temp_node.right)
            
            current_count -= 1
    



# Root
root = Node(4)

# 1st Level
root.left      = Node(5)
root.right     = Node(2)

# 2nd Level
root.right.left  = Node(3)
root.right.right = Node(1)

# 3rd Level
root.right.left.left  = Node(6)
root.right.left.right = Node(7)

print("Left View of Binary Tree: ")
left_view_binary_tree(root)
print()