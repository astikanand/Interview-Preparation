class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

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


def search(root, key):
    # If root is None, then key doesn't exist.
    if root is None:
        return False
    
    # If root's val matches the key, then we have found the key in 
    if(root.val == key):
        return True
    
    # If key is lesser than root's val search in left subtree else serach in right subtree.
    if(key < root.val):
        return search(root.left, key)
    else:
        return search(root.right, key)


def print_bst_inorder(root):
    if(root):
        print_bst_inorder(root.left)
        print(root.val, end=" ")
        print_bst_inorder(root.right)
    


print("Inserting 8, 3, 10, 1, 6, 14, 4, 7, 13 into BST")
root = Node(8)
insert(root, 3)
insert(root, 10)
insert(root, 1)
insert(root, 6)
insert(root, 14)
insert(root, 4)
insert(root, 7)
insert(root, 13)
print("BST Now:")
print_bst_inorder(root)
print("\n")

print("Searching if 5 is present ? : {}".format(search(root, 5)))
print("Searching if 6 is present ? : {}".format(search(root, 6)))