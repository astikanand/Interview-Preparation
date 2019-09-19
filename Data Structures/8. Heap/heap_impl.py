def max_heapify(arr, i, N):
    left_child = 2*i+1
    right_child = 2*i+2

    # Find the largest of left_child, right_child and parent which is i.
    largest = left_child if left_child < N and arr[left_child] > arr[i] else i
    largest = right_child  if right_child < N and arr[right_child] > arr[largest]

    # If Parent is not largest, swap and apply max_heapify on child to propagate it down
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, N)
      

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        max_heapify(arr, i, n)
    
    return arr
    
