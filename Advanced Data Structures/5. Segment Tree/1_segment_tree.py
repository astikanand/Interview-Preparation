from math import pow, ceil, log

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        n = len(arr)
        x = int(pow(2, ceil(log(n, 2))))
        self.tree = ['-∞']*(2*x)
        

    # We will build a segment tree using recursion (bottom-up approach).
    # Each leaf will have a single element and all the internal nodes will have sum of both of its children.
    # Complexity: O(N) as total node are appox 4N
    # Auxilliary Space: O(N) as total required are 3N extra.
    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            # Build for left child
            self.build_tree(2*node, start, mid)
            # Build for right child
            self.build_tree(2*node+1, mid+1, end)
            # Internal node will have the sum of both of its children
            self.tree[node] = self.tree[2*node] + self.tree[2*node + 1]
    

    # To query on a given range, we need to check 3 conditions, explained below with cases.
    # node : [start, end]   and   given_range : [left, right]
    # Complexity: O(logN)
    def query(self, node, start, end, left, right):
        # Case-1: Range represented by the node is completely outside the given range
        if(right < start or end < left):
            return 0
        
        # Case-2: Range represented by the node is completely inside the given range
        if(left <= start and end <= right):
            return self.tree[node]
        
        # Case-3: Range represented by a node is partially inside and partially outside the given range
        mid = (start + end) // 2
        val_1 = self.query(2*node, start, mid, left, right)
        val_2 = self.query(2*node+1, mid+1, end, left, right)

        return val_1 + val_2
    

    # To update an element we need to look at the interval in which the element is and recurse 
    # accordingly on the left or the right child.
    # Complexity: O(logN)
    def update(self, node, start, end, index, val_diff):
        if start == end:
            self.tree[node] += val_diff
        else:
            mid = (start + end) // 2
            if start <= index and index <= mid:
                self.update(2*node, start, mid, index, val_diff)
            else:
                self.update(2*node+1, mid+1, end, index, val_diff)

            # Internal node will have the sum of both of its children
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    


# Driver Program
seg_tree = SegmentTree([1, 3, 5, 7, 9, 11])
seg_tree.build_tree(1, 0, 5)
print("Newly Built Segment Tree:")
print(seg_tree.tree)
print("Sum in Range [1, 3] : {}".format(seg_tree.query(1, 0, 5, 1, 3 )))

print("\nUpdating index 1 from 3 to 10: increment by 7.")
seg_tree.update(1, 0, 5, 1, 7)
print("Segment Tree after Update:")
print(seg_tree.tree)
print("Sum in Range [1, 3] after update: {}".format(seg_tree.query(1, 0, 5, 1, 3 )))
