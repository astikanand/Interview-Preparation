def heap_sort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2, -1, -1): 
        max_heapify(arr, i, n) 
  
    # One by one move larger elements to end and decrease the size
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        max_heapify(arr, 0, i)
    
    return arr


def max_heapify(arr, i, N):
    left_child = 2*i+1
    right_child = 2*i+2

    # Find the largest of left_child, right_child and parent which is i.
    if (left_child < N and arr[left_child] > arr[i]):
        largest = left_child
    else:
        largest = i

    if (right_child < N and arr[right_child] > arr[largest]):
         largest = right_child

    # If Parent is not largest, swap and apply max_heapify on child to propagate it down
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, N)
  


print("Example-1: heap_sort(arr)")
arr = [10, 80, 30, 90, 70, 85, 75, 95, 40, 50, 70]
print(heap_sort(arr))

print("Example-2: heap_sort(arr)")
arr = [4, 3, 2, 10, 12, 1, 5, 6]
print(heap_sort(arr))

print("Example-3: heap_sort(arr)")
arr = [12, 11, 13, 5, 6]
print(heap_sort(arr))