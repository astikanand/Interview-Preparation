from math import pow, ceil, log

class LazySegmentTree:
    def __init__(self, arr):
        self.arr = arr
        n = len(arr)
        x = int(pow(2, ceil(log(n, 2))))
        self.tree = ['-∞']*(2*x)
        self.lazy = [0]*(2*x)
        

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
    

    def lazy_update(self, node, start, end, left, right, val):
        # Case-1: If the interval represented by current node has pending updates, 
        # then update the current node, mark children as lazy and reset the current lazy node.
        if self.lazy[node] != 0:
            self.tree[node] += (end-start+1)*self.lazy[node]
            if start != end:
                self.lazy[2*node] += self.lazy[node]       # Mark left child lazy
                self.lazy[2*node+1] += self.lazy[node]     # Mark right child lazy
            
            # Reset the lazy node 
            self.lazy[node] = [0]
        
        # Case-2: If the interval represented by current node lies completely outside the given interval
        # to update, then ignore it.
        if (start > end or right < start or end < left):
            return
        
        # Case-3: If the interval represented by current node lies completely in the given interval to update, 
        # then update the current node and mark children as lazy.
        if (left <= start and end <= right):
            self.tree[node] += (end-start+1)*val
            if start != end:
                # Mark children as lazy
                self.lazy[2*node] += val               # Mark left child lazy
                self.lazy[2*node+1] += val             # Mark right child lazy

            return
        
        # Case-4: If the interval represented by current node overlaps with the given interval to update, 
        # then update the both children recursively and finally update the current node.
        mid = (start + end) // 2
        self.lazy_update(2*node, start, mid, left, right, val)       # Updating left child
        self.lazy_update(2*node+1, mid+1, end, left, right, val)     # Updating right child 
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]    # Updating  using children
    

    def lazy_query(self, node, start, end, left, right):
        # Case-1: If the interval represented by current node has pending updates, 
        # then update the current node, mark children as lazy and reset the current lazy node.
        if self.lazy[node] != 0:
            self.tree[node] += (end-start+1)*self.lazy[node]
            if start != end:
                self.lazy[2*node] += self.lazy[node]       # Mark left child lazy
                self.lazy[2*node+1] += self.lazy[node]     # Mark right child lazy
            
            # Reset the lazy node 
            self.lazy[node] = [0]
        
        # Case-2: If the interval represented by current node lies completely outside the given interval 
        # to query, then return 0.
        if (start > end or right < start or end < left):
            return 0
        
        # Case-3: If the interval represented by current node lies completely inside the given interval 
        # to query, then simply return the current node value.
        if (left <= start and end <= right):
            return self.tree[node]
        
        # Case-4: If the interval represented by current node overlaps with the given interval to query, 
        # query the left and right child and return the total of both.
        mid = (start + end) // 2
        val_1 = self.lazy_query(2*node, start, mid, left, right);         # Query left child
        val_2 = self.lazy_query(2*node+1, mid+1, end, left, right);        # Query right child

        return val_1 + val_2



# Driver Program
lazy_seg_tree = LazySegmentTree([1, 3, 5, 7, 9, 11])
lazy_seg_tree.build_tree(1, 0, 5)
print("Newly Built Lazy Segment Tree:")
print("Tree: {}".format(lazy_seg_tree.tree))
print("Lazy Arr: {}".format(lazy_seg_tree.lazy))
print("Sum in Range [1, 3] : {}".format(lazy_seg_tree.lazy_query(1, 0, 5, 1, 3 )))

print("\nUpdate by adding 10 to all nodes at indexes from 1 to 5")
lazy_seg_tree.lazy_update(1, 0, 5, 1, 5, 10)
print("Lazy Segment Tree after Update:")
print("Tree: {}".format(lazy_seg_tree.tree))
print("Lazy Arr: {}".format(lazy_seg_tree.lazy))
print("Sum in Range [1, 3] after update: {}".format(lazy_seg_tree.lazy_query(1, 0, 5, 1, 3 )))
