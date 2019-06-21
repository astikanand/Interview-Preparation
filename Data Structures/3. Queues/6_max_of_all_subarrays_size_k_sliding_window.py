def max_of_all_subarrays_of_k_size(arr, k):
    n = len(arr)
    max_subarray = []

    # Initially current window
    current_window = arr[:k]

    # First get the initial current_window of of first k elements,
    # the first element of max_subarray is max of initial window.
    max_subarray.append(max(current_window))

    # Now start from k+1th element, and in current_window
    # dequeue the first element from current_window and enqueue the k+1th element
    # get max of current_window and put in max_subarray and continue till the last element.
    for i in range(k, n):
        # Dequeue the first element and enqueue the next element
        current_window.pop(0)
        current_window.append(arr[i])

        max_subarray.append(max(current_window))
    
    return max_subarray



print("Example-1: max_of_all_subarrays_of_k_size")
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(max_of_all_subarrays_of_k_size(arr, 3))

print("\nExample-2: max_of_all_subarrays_of_k_size")
arr = [8,  5,  10, 7,  9,  4,  15, 12, 90, 13]
print(max_of_all_subarrays_of_k_size(arr, 4))