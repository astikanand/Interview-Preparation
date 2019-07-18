class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    

def are_identical(root1, root2):
    # If both are NULL, then True.
    if root1 is None and root2 is None:
        return True
    
    # If one is None and other not None, then False.
    if root1 is None or root2 is None:
        return False
    
    # Check if the val of both roots is same and left subtree and right subtree are are_identical.
    return (root1.val==root2.val and are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right))


def is_subtree(S, T):
    # If S is None, always subtree.
    if S is None:
        return True
    
    # If S is not None and T is none, not a subtree.
    if T is None:
        return False
    
    # If both are identical return True.
    if are_identical(S, T):
        return True
    else:
        # Check if any of T.left or T.right is identical to S.
        return are_identical(S, T.left) or are_identical(S, T.right)


 

# Tree S
S = Node(10)
S.left   = Node(4)
S.right  = Node(6)
S.left.right = Node(30)

# Tree T
T = Node(26)
T.left   = Node(10)
T.right  = Node(3)
T.left.left   = Node(4)
T.left.right  = Node(6)
T.right.right = Node(3)
T.left.left.right = Node(30)

print("Is Tree S subtree of Tree T ?: {}".format(is_subtree(S, T)))
