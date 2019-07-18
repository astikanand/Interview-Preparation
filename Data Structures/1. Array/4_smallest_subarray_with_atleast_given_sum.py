def smallest_subarray_with_atleast_given_sum(arr, x):
    n = len(arr)
    # Initialize current sum and minimum length 
    current_sum = 0; min_length = n + 1
  
    # Initialize starting and ending indexes 
    start = 0; end = 0
    final_start = 0; final_end = 0

    # Take all the elements one by one while end is smaller than n.
    while (end < n): 
        # Keep adding array elements while current sum is smaller than x and increment end 
        while (current_sum <= x and end < n): 
            current_sum += arr[end] 
            end += 1
  
        # Once current_sum becomes greater than x, start removing the trailing statement
        # Update the min_length if needed and increment start
        while (current_sum > x and start < n): 
            if (end - start < min_length): 
                min_length = end - start
                final_start = start
                final_end = end 

            current_sum -= arr[start] 
            start+= 1
      
    if(min_length == n+1):
        print("No Subarray Possible for given sum: {}".format(x))
    else:
        print("Min Length: {} and Subarray: {} for given sum: {}".format(min_length, arr[final_start:final_end], x))



print("Example-1: smallest_subarray_with_atleast_given_sum([1, 4, 45, 6, 0, 19], 51)")
smallest_subarray_with_atleast_given_sum([1, 4, 45, 6, 0, 19], 51)

print("\nExample-2: smallest_subarray_with_atleast_given_sum([1, 10, 5, 2, 7], 9)")
smallest_subarray_with_atleast_given_sum([1, 10, 5, 2, 7], 9)

print("\nExample-3: smallest_subarray_with_atleast_given_sum([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280)")
smallest_subarray_with_atleast_given_sum([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280)

print("\nExample-4: smallest_subarray_with_atleast_given_sum([1, 2, 4], 8)")
smallest_subarray_with_atleast_given_sum([1, 2, 4], 8)
