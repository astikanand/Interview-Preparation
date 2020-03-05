def maximum_sum_subarray_kadane(arr):
    n = len(arr)
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start = 0; end = 0; s = 0;

    for i in range(1, n):
        max_ending_here += arr[i]
        
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here
            start = s
            end = i
        
        if(max_ending_here < 0):
            max_ending_here = 0
            s = i+1
        
    
    return (max_so_far, arr[start:end+1])



print("Example-1: maximum_sum_subarray_kadane(arr)")
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum, subarray = maximum_sum_subarray_kadane(arr)
print("Max: {} and Subarray: {}".format(max_sum, subarray))

print("\nExample-2: maximum_sum_subarray_kadane(arr)")
arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
max_sum, subarray = maximum_sum_subarray_kadane(arr)
print("Max: {} and Subarray: {}".format(max_sum, subarray))

print("\nExample-3: maximum_sum_subarray_kadane(arr)")
arr = [-2, 1]
max_sum, subarray = maximum_sum_subarray_kadane(arr)
print("Max: {} and Subarray: {}".format(max_sum, subarray))
