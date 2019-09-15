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


def delete_key(root, k):
    # If root is NULL, return new node
    if root is None:
        return root

    # Splay the given key k and find the root
    root = splay(root, k)

    # If root we got doesn't has the key same as k, nothing to delete, return root.
    if root.key != k:
        return root
    else:
        # Split the tree into two trees, delete the root node
        root1 = root.left
        root2 = root.right
        del root

        # If root1 is NULL, return root2
        if root1 is None:
            return root2
        else:
            # Splay tree1 with key=k to get max on top
            root1 = splay(root1, k)
            root1.right = root2     # Make root2 as right child of root1

            return root1
            

def print_preorder(root):
    if root:
        print(root.key, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)



print("Splay Tree Delete Example:")
root = Node(6) 
root.left = Node(1) 
root.right = Node(9) 
root.left.right = Node(4) 
root.right.left = Node(7) 
root.left.right.left = Node(2)

print("Initial Splay Tree - PreOrder:")
print_preorder(root)
print() 
print("\nSplay Tree after 4 was deleted - PreOrder:")   
root = delete_key(root, 4)
print_preorder(root)
print()
