class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def right_rotate(current_pivot):
    new_pivot = current_pivot.left
    temp = new_pivot.right
    new_pivot.right = current_pivot
    current_pivot.left = temp

    return new_pivot


def left_rotate(current_pivot):
    new_pivot = current_pivot.right
    temp = new_pivot.left
    new_pivot.left = current_pivot
    current_pivot.right = temp

    return new_pivot


def splay(root, key):
    # Node is already Root
    if root is None or root.key == key:
        return root
    
    # Node is present if left subtree
    if key < root.key:
        # key is not in tree, we are done - return the last accessed 
        if root.left is None:
            return root
        
        # Zig-Zig (Left Left) Case
        if key < root.left.key:
            # First recursively bring the key as root of left-left  
            root.left.left = splay(root.left.left, key)
            root = right_rotate(root)  # First Rotation of root
        
        # Zag-Zig (Left Right) Case
        elif key > root.left.key:
            # First recursively bring the key as root of left-right  
            root.left.right = splay(root.left.right, key)

            if root.left.right:
                root.left = left_rotate(root.left)  # First Rotation for root-left
        
        return root if root.left is None else right_rotate(root)
    
    # Node is present in right subtree
    else:
        # key is not in tree, we are done - return the last accessed 
        if root.right is None:
            return root
        
        # Zag-Zag (Right Right Case)
        if key > root.right.key:
            # First recursively bring the key as root of right-right 
            root.right.right = splay(root.right.right, key)
            root = left_rotate(root)  # First Rotation of root
        
        # Zig-Zag (Right Left) Case
        elif key < root.right.key:
            # First recursively bring the key as root of right-left
            root.right.left = splay(root.right.left, key)

            if root.right.left:
                root.right = right_rotate(root.right) # First rotation of root-right
        
        return root if root.right is None else left_rotate(root)


def search_key(root, k):
    return splay(root, k)


def print_preorder(root):
    if root:
        print(root.key, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)



print("Splay Tree Search Example:")
root = Node(100) 
root.left = Node(50) 
root.right = Node(200) 
root.left.left = Node(40) 
root.left.left.left = Node(30) 
root.left.left.left.left = Node(20)

print("Initial Splay Tree - PreOrder:")
print_preorder(root)
print() 
print("\nSplay Tree after 20 was searched - PreOrder:")   
root = search_key(root, 20)
print_preorder(root)
print()
