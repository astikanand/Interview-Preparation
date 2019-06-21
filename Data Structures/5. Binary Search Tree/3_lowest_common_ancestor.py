class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor(root, key1, key2):
    while(root):
        # If both key1 and key2 is smaller than root's val, then lca exist in left subtree.
        if(key1 < root.val and key2 < root.val):
            root = root.left
        # If both key1 and key2 is greater than root's val, then lca exist in right subtree.
        elif(key1 > root.val and key2 > root.val):
            root = root.right
        # Else this root is LCA.
        else:
            break
    
    return root.val
        


root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10)
root.left.right.right = Node(14) 
print("Lowest Common Ancestor of 10 and 14 is : {}".format(lowest_common_ancestor(root, 10, 14)))
print("Lowest Common Ancestor of 14 and 8 is : {}".format(lowest_common_ancestor(root, 14, 8)))
print("Lowest Common Ancestor of 10 and 22 is : {}".format(lowest_common_ancestor(root, 10, 22)))