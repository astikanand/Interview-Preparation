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
