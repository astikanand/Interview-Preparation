import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize -1

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Function to find height of a tree 
def height(root, ans):
    if root is None:
        return 0
 
    left_height = height(root.left, ans)
    right_height = height(root.right, ans)
 
    # update the answer, because diameter of a tree is nothing but maximum value of
    # (left_height + right_height + 1) for each node
    ans[0] = max(ans[0], 1 + left_height + right_height)
 
    return 1 + max(left_height, right_height)
 

# Computes the diameter of binary tree with given root.
def diameter(root):
    if root is None:
        return 0
        
    ans = [INT_MIN] # This will store the final answer
    height_of_tree = height(root, ans)
    return ans[0]
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
 
print ("Diameter of the tree is %d" %(diameter(root)))