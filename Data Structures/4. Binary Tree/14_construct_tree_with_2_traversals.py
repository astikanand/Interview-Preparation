class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
 
# Recursive function to construct binary of size len from 
# Inorder traversal inorder[] and Preorder traversal preorder[].  
# Initial values of inorder_start and inorder_end should be 0 and len -1.  
# The function doesn't do any error checking for cases where inorder and preorder do not form a tree.
def build_tree(inorder, preorder, inorder_start, inorder_end):
    if (inorder_start > inorder_end):
        return None
 
    # Pick current node from Preorder traversal using preorder_index and increment preorder_index
    # Create a new tree node with this picked element
    tree_node = Node(preorder[build_tree.preorder_index])
    build_tree.preorder_index += 1
 
    # If this node has no children then return
    if inorder_start == inorder_end :
        return tree_node
 
    # Else find the index of this node in Inorder traversal
    inorder_index = search(inorder, inorder_start, inorder_end, tree_node.val)
     
    # Using index in Inorder Traversal, construct left and right subtrees
    tree_node.left = build_tree(inorder, preorder, inorder_start, inorder_index-1)
    tree_node.right = build_tree(inorder, preorder, inorder_index+1, inorder_end)
 
    return tree_node


# Function to find index of vaue in arr[start...end]
# The function assumes that value is rpesent in inorder[]
def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i
 
def inorder_traversal(node):
    if node is None:
        return
     
    inorder_traversal(node.left)
    print (node.val, end=" ")
    inorder_traversal(node.right)



# Driver program to test above function
inorder = ['D', 'B' ,'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preorder_index
build_tree.preorder_index = 0
root = build_tree(inorder, preorder, 0, len(inorder)-1)
 
# Let us test the build tree by priting Inorder traversal
print ("Inorder traversal of the constructed tree is:")
inorder_traversal(root)
print()
