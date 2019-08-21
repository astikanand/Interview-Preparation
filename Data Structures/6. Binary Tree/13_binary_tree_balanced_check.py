class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None
  
class Height: 
    def __init__(self): 
        self.height = 0
  

def isBalanced(root, height): 
    # lh and rh to store height of left and right subtree 
    lh = Height() 
    rh = Height() 

    if root is None: 
        return True
  
    # l and r are used to check if left and right subtree are balanced 
    l = isBalanced(root.left, lh) 
    r = isBalanced(root.right, rh)

    # Update height
    height.height = max(lh.height, rh.height) + 1
  
    if abs(lh.height-rh.height) <= 1 and l and r: 
        return True
  
    # if we reach here then the tree is not balanced 
    return False
  

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.left.left.left = Node(7) 
  
if isBalanced(root, Height()): 
    print('Tree is balanced') 
else: 
    print('Tree is not balanced')