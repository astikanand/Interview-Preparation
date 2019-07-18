class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


def insert(root, key):
    ###### Step-1: Perform Normal BST insertion.
    if not root: 
        return Node(key) 
    elif key < root.val: 
        root.left = insert(root.left, key) 
    else: 
        root.right = insert(root.right, key) 
    

    ###### Step-2: Update the height of the ancestor node. 
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    ###### Step-3: Get the balance factor.
    balance = get_balance_factor(root)

    ###### Step-4: If the node is unbalanced, then try out the 4 cases discussed.
    ### a) Left Left Case:
    if balance < -1 and key < root.left.val: 
        return right_rotate(root)
    
    ### b) Left Right Case:
    if balance < -1 and key > root.left.val: 
        root.left = left_rotate(root.left) 
        return right_rotate(root)
    
    ### c) Right Right Case:
    if balance > 1 and key > root.right.val: 
        return left_rotate(root)
    
    ### d) Right Left Case:
    if balance > 1 and key < root.right.val: 
        root.right = right_rotate(root.right) 
        return left_rotate(root)
    
    return root


def delete(root, key):
    ###### Step-1: Perform Normal BST deletion.
    if not root: 
        return root 
    elif key < root.val: 
        root.left = delete(root.left, key) 
    elif key > root.val: 
        root.right = delete(root.right, key) 
    else: 
        if root.left is None: 
            temp = root.right 
            root = None
            return temp 
        elif root.right is None: 
            temp = root.left 
            root = None
            return temp 
        
        temp = min_node(root.right) 
        root.val = temp.val 
        root.right = delete(root.right, temp.val) 

    ###### If the tree has only one node simply return it 
    if root is None: 
        return root 
    

    ###### Step-2: Update the height of the ancestor node. 
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    ###### Step-3: Get the balance factor.
    balance = get_balance_factor(root)

    ###### Step-4: If the node is unbalanced, then try out the 4 cases discussed.
    ### a) Left Left Case:
    if balance < -1 and key < root.left.val: 
        return right_rotate(root)
    
    ### b) Left Right Case:
    if balance < -1 and key > root.left.val: 
        root.left = left_rotate(root.left) 
        return right_rotate(root)
    
    ### c) Right Right Case:
    if balance > 1 and key > root.right.val: 
        return left_rotate(root)
    
    ### d) Right Left Case:
    if balance > 1 and key < root.right.val: 
        root.right = right_rotate(root.right) 
        return left_rotate(root)
    
    return root


def right_rotate(current_pivot):
    # current_pivot's left will become the new_pivot
    # new_pivot's right will change so store it as T2.
    new_pivot = current_pivot.left 
    T2 = new_pivot.right 

    # Perform rotation: Change the new_pivot's right as current pivot
    # and then make current pivot's left T2
    new_pivot.right = current_pivot 
    current_pivot.left = T2 

    # Update heights for both pivot and new_pivot
    current_pivot.height = 1 + max(get_height(current_pivot.left), get_height(current_pivot.right)) 
    new_pivot.height = 1 + max(get_height(new_pivot.left), get_height(new_pivot.right)) 

    # Return the new root 
    return new_pivot


def left_rotate(current_pivot):
    # current_pivot's right will become the new_pivot
    # new_pivot's left will change so store it as T2.
    new_pivot = current_pivot.right 
    T2 = new_pivot.left 

    # Perform rotation: Change the new_pivot's left as current pivot
    # and then make current pivot's right T2
    new_pivot.left = current_pivot 
    current_pivot.right = T2 

    # Update heights for both pivot and new_pivot
    current_pivot.height = 1 + max(get_height(current_pivot.left), get_height(current_pivot.right)) 
    new_pivot.height = 1 + max(get_height(new_pivot.left), get_height(new_pivot.right)) 

    # Return the new root 
    return new_pivot 


def get_height(node):
    if node is None:
        return 0
    return node.height


def get_balance_factor(node):
    if node is None:
        return 0
    return get_height(node.right) - get_height(node.left)


def min_node(current_node):
    # If current_node is None, min_node not possible
    if(current_node is None):
        return None
    
    min_node = current_node
    while(min_node.left):
        min_node = min_node.left
    
    return min_node


def print_preorder(root):
    if root:
        print(root.val, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)


print("Print the AVL TREE Traversal:")
root = None
root = insert(root, 10) 
root = insert(root, 20) 
root = insert(root, 30) 
root = insert(root, 40) 
root = insert(root, 50) 
root = insert(root, 25)
print_preorder(root)
print()
print("\nAVL Tree after deleting Node 40:")
root = delete(root, 40)
print_preorder(root)
print()