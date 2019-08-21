def longest_increasing_subarray(arr):
    n = len(arr) 
    max_length = curr_length = 1 
       
    for i in range(1, n): 
        if (arr[i] > arr[i-1]) : 
            curr_length += 1 
        else: 
            max_length = max(curr_length, max_length) 
            curr_length = 1 

    max_length = max(curr_length, max_length)
       
    return max_length 
  


arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
print("Length = ", longest_increasing_subarray(arr))