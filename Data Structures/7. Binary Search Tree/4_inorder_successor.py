class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_successor(root, key):
    # Get the given node by search using key.
    given_node = search(root, key)

    # If given_node's right exist, simply return the min_node from right.
    if(given_node.right):
        return min_node(given_node.right)
    
    # Set successor as None and start from root and search for successor by travelling down the tree.
    successor = None
    while(root):
        # If given_node’s data < root’s data then go left side and update the successor.
        # given_node हमेशा successor के left subtree में होना चाहिए, इसलिए successor तभी update करेंगे जब left subtree में जाएंगे ।
        if(given_node.val < root.val):
            successor = root
            root = root.left
        # Else if a given_node’s data < root’s data then go to right side.
        elif (given_node.val > root.val):
            root = root.right
        # Else break when given_node’s data and root’s data are equal, given_node is found.
        else:
            break
    
    # Finally return the successor.
    return successor

        

def search(root, key):
    # If root is None, then key doesn't exist.
    if root is None:
        return root
    
    # If root's val matches the key, then we have found the key in 
    if(root.val == key):
        return root
    
    # If key is lesser than root's val search in left subtree else serach in right subtree.
    if(key < root.val):
        return search(root.left, key)
    else:
        return search(root.right, key)


def min_node(current_node):
    # If current_node is None, min_node not possible
    if(current_node is None):
        return None
    
    min_node = current_node
    while(min_node.left):
        min_node = min_node.left
    
    return min_node



root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10)
root.left.right.right = Node(14) 
print("Inorder Successor of  8 is : {}".format(inorder_successor(root, 8).val))
print("Inorder Successor of 10 is : {}".format(inorder_successor(root, 10).val))
print("Inorder Successor of 14 is : {}".format(inorder_successor(root, 14).val))
