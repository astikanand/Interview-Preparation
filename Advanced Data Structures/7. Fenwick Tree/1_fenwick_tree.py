class FenwickTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.fenwick_tree = [0]*(self.n+1)

        for i in range(self.n):
            self.update_tree(i, arr[i])
        
    
    def update_tree(self, i, val): 
        i += 1       # index in fenwick_tree[] is 1 more than the index in arr[]

        # Traverse all ancestors and add 'val' 
        while i <= self.n: 
            self.fenwick_tree[i] += val        # Add 'val' to current node of Fenwick Tree 
            i += i & (-i)         # Move index to that of parent node in Logical Update View Tree
    

    def get_sum(self, i):
        total_sum = 0
        i += 1
    
        # Traverse ancestors of fenwick_tree[index] and the value to sum
        while i > 0:  
            total_sum += self.fenwick_tree[i]      # Add current element of fenwick_tree to sum 
            i -= i & (-i)          # Move index to that of parent node in Logical Query / Get Sum View Tree

        return total_sum



print("Fenwick Tree Example:")
arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
fen_tree = FenwickTree(arr)
print("Sum of elements in arr[0..5] is : {}".format(fen_tree.get_sum(5)))
fen_tree.update_tree(3, 6)
print("Sum of elements in arr[0..5] after update_tree is : {}".format(fen_tree.get_sum(5)))