class IntervalTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None


def insert(root, low, high):
    if not root:
        return IntervalTreeNode(low, high)
    
    if low <= root.low:
        root.left = insert(root.left, low, high)
    else:
        root.right = insert(root.right, low, high)
    
    return root


def find_conflicting_appointment(root, low, high):
    while root:
        if(root.low < high and low < root.high):
            print("[{}, {}] Conflicts with [{}, {}]".format(low, high, root.low, root.high))
            return
        elif low <= root.low:
            root = root.left
        else:
            root = root.right


def conflicting_appointments(root, appointments):
    for appointment in appointments:
        low = appointment[0]
        high = appointment[1]
        find_conflicting_appointment(root, low, high)
        root = insert(root, low, high)



print("Exampl-1: Conflicting Appointments - Interval Tree")
appointments = [(1, 5), (3, 7), (2, 6), (10, 15), (5, 6), (4, 100)] 
conflicting_appointments(None, appointments)
