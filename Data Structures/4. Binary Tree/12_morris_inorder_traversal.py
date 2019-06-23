class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def morris_inorder_traversal(root):
    current = root 
     
    while(current is not None):
        if current.left is None:
            print(current.val, end=" ")
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while(pre.right is not None and pre.right != current):
                pre = pre.right
  
            # Make current as right child of its inorder predecessor
            if(pre.right is None):
                pre.right = current
                current = current.left
                 
            # Revert the changes made in if part to restore the 
            # original tree i.e., fix the right child of predecssor
            else:
                pre.right = None
                print(current.val, end=" ")
                current = current.right
    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
morris_inorder_traversal(root)