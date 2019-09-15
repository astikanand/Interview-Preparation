def longest_increasing_subarray(arr):
    n = len(arr) 
    max_length = curr_length = 1
    end = 0
       
    for i in range(1, n): 
        if (arr[i] > arr[i-1]) : 
            curr_length += 1 
        else:
            if(curr_length > max_length):
                max_length = curr_length
                end = i
                curr_length = 1 

    if(curr_length > max_length):
        max_length = curr_length
        end = i

    print("Longest Increasing Subarray: {}".format(arr[end-max_length:end]))
  


print("Example-1: longest_increasing_subarray([5, 6, 3, 5, 7, 8, 9, 1, 2])")
longest_increasing_subarray([5, 6, 3, 5, 7, 8, 9, 1, 2])

print("\nExample-2: longest_increasing_subarray([12, 13, 1, 5, 4, 7, 8, 10, 10, 11])")
longest_increasing_subarray([12, 13, 1, 5, 4, 7, 8, 10, 10, 11])
