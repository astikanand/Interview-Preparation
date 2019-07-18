def heap_sort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    # Initialize largest as root 
    largest = i 

    # Childs: left = 2*i + 1  right = 2*i + 2   
    l = 2*i+1
    r = 2*i+2
  
    # If left child of root exists and is greater than root 
    if l<n and arr[l]>arr[i]: 
        largest = l 
  
    # If right child of root exists and is greater than root 
    if r<n and arr[r]>arr[largest]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]   # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  


print("Example-1: heap_sort(arr)")
arr = [10, 80, 30, 90, 70, 85, 75, 95, 40, 50, 70]
print(heap_sort(arr))

print("Example-2: heap_sort(arr)")
arr = [4, 3, 2, 10, 12, 1, 5, 6]
print(heap_sort(arr))

print("Example-3: heap_sort(arr)")
arr = [12, 11, 13, 5, 6]
print(heap_sort(arr))
