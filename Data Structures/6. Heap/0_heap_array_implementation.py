import sys
from heapq import heappush, heappop, heapify  

# Heap functions from python library  
#   • heappop - pop and return the smallest element from heap 
#   • heappush - push the value item onto the heap, maintaining heap invarient 
#   • heapify - transform list into heap, in place, in linear time 

MIN = -sys.maxsize-1
  

class MinHeap:
    def __init__(self): 
        self.heap = []  
  
    def parent(self, i): 
        return int((i-1)/2)
      
    # Inserts a new key 'k' 
    def insertKey(self, k): 
        heappush(self.heap, k)            
  
    # Decrease value of key at index 'i' to new_val 
    # It is assumed that new_val is smaller than heap[i] 
    def decreaseKey(self, i, new_val): 
        self.heap[i]  = new_val  
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
            # Swap heap[i] with heap[parent(i)] 
            self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i] 
              
    # Method to remove minium element from min heap 
    def extractMin(self): 
        return heappop(self.heap) 
  
    # This functon deletes key at index i. It first reduces 
    # value to minus infinite and then calls extractMin() 
    def deleteKey(self, i): 
        self.decreaseKey(i, MIN) 
        self.extractMin() 
  
    # Get the minimum element from the heap 
    def getMin(self): 
        return self.heap[0] 
  


print("Example:- Array Implementation of Heap")
print("InsertKey: 3, 2 then DeleteKey: 1 and then InsertKey: 15, 5, 4, 45")
my_heap = MinHeap() 
my_heap.insertKey(3) 
my_heap.insertKey(2) 
my_heap.deleteKey(1) 
my_heap.insertKey(15) 
my_heap.insertKey(5) 
my_heap.insertKey(4) 
my_heap.insertKey(45)

print("Extracted Min = {}".format(my_heap.extractMin()))
print("Get Min = {}".format(my_heap.getMin()))
my_heap.decreaseKey(2, 1) 
print("After Decreasing Key of 2 to 1, Now Get Min = {}".format(my_heap.getMin()))
