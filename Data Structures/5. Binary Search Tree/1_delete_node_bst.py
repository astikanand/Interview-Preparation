class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def delete(root, key):
    # Check if root None: key doesn't exist, not possible to delete.
    if root is None:
        return root
    
    # If key is lesser than root.val: Delete the key in left subtree.
    if(key < root.val):
        root.left = delete(root.left, key)
    # If key is greater than root.val: Delete the key in right subtree.
    elif(key > root.val):
        root.right = delete(root.right, key)
    # If key is equal to root.val: Need to delete this root node.
    else:
        # If no child exists: make root None and return None.
        if(root.left is None and root.right is None):
            root = None
            return None
        # If left child exists: make root None and return left child.
        elif(root.right is None):
            temp = root.left
            root = None
            return temp
        # If right child exists: make root None and return the right child.
        elif(root.left is None):
            temp = root.right
            root = None
            return temp
        # If both child exists:
        else:
            # Get the min_node from right child subtree.
            temp = min_node(root.right)
            # Set the val of root as the val of min node.
            root.val = temp.val
            # Delete the min node from right subtree.
            root.right = delete(root.right, temp.val)
    
    # Finally return the root.
    return root
    
    


def min_node(current_node):
    # If current_node is None, min_node not possible
    if(current_node is None):
        return None
    
    min_node = current_node
    while(min_node.left):
        min_node = min_node.left
    
    return min_node


def insert(root, key):
    if(root is None):
        root = Node(key)
    
    # If key is lesser than root.val insert key in left subtree
    if(key <= root.val):
        if(root.left is None):
            root.left = Node(key)
        else:
            insert(root.left, key)
    # If key is greater than root.val insert key in right subtree
    else:
        if(root.right is None):
            root.right = Node(key)
        else:
            insert(root.right, key)



def print_bst_inorder(root):
    if(root):
        print_bst_inorder(root.left)
        print(root.val, end=" ")
        print_bst_inorder(root.right)
    


print("Insert:- 50, 30, 70, 20, 40, 60, 80 into BST.")
root = Node(50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)
print("BST at start:")
print_bst_inorder(root)
print("\n")

delete(root, 20)
print("BST after deleting 20:")
print_bst_inorder(root)
print()

delete(root, 30)
print("BST after deleting 30:")
print_bst_inorder(root)
print()

delete(root, 50)
print("BST after deleting 50:")
print_bst_inorder(root)
print()