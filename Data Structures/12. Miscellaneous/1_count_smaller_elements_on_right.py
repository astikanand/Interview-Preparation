class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1


def insert(root, key):
    ###### Step-1: Perform Normal BST insertion.
    if not root: 
        return Node(key) 
    elif key < root.val: 
        root.left = insert(root.left, key) 
    else:
        root.right = insert(root.right, key)
        # Update the count_smaller for the key
        count_smaller[key] += size(root.left) + 1
    
    ###### Step-2: Update the height and size of the ancestor node. 
    root.height = 1 + max(height(root.left), height(root.right))
    root.size = 1 + size(root.left) + size(root.right)

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
    current_pivot.height = 1 + max(height(current_pivot.left), height(current_pivot.right)) 
    new_pivot.height = 1 + max(height(new_pivot.left), height(new_pivot.right))

    # Update sizes for both pivot and new_pivot
    current_pivot.size = 1 + size(current_pivot.left) + size(current_pivot.right) 
    new_pivot.size = 1 + size(new_pivot.left) + size(new_pivot.right) 

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
    current_pivot.height = 1 + max(height(current_pivot.left), height(current_pivot.right)) 
    new_pivot.height = 1 + max(height(new_pivot.left), height(new_pivot.right))

    # Update sizes for both pivot and new_pivot
    current_pivot.size = 1 + size(current_pivot.left) + size(current_pivot.right) 
    new_pivot.size = 1 + size(new_pivot.left) + size(new_pivot.right) 

    # Return the new root 
    return new_pivot 


def height(node):
    if node is None:
        return 0
    return node.height


def size(node):
    if node is None:
        return 0
    return node.size


def get_balance_factor(node):
    if node is None:
        return 0
    return height(node.right) - height(node.left)


def min_node(current_node):
    # If current_node is None, min_node not possible
    if(current_node is None):
        return None
    
    min_node = current_node
    while(min_node.left):
        min_node = min_node.left
    
    return min_node


def count_smaller_elements_on_right(arr):
    n = len(arr)
    root = None

    for i in range(n-1, -1, -1):
        count_smaller[arr[i]] = 0
        root = insert(root, arr[i])
    
    for i in arr:
        print(count_smaller[i], end=" ")
    
    print()
    count_smaller.clear()


count_smaller = {}
print("Example-1: count_smaller_elements_on_right([10, 6, 15, 20, 30, 5, 7])")
count_smaller_elements_on_right([10, 6, 15, 20, 30, 5, 7])

print("\nExample-2: count_smaller_elements_on_right([5, 4, 3, 2, 1])")
count_smaller_elements_on_right([5, 4, 3, 2, 1])

print("\nExample-3: count_smaller_elements_on_right([1, 2, 3, 4, 5])")
count_smaller_elements_on_right([1, 2, 3, 4, 5])
