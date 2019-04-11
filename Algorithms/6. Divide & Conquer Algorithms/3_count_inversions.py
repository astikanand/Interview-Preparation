def count_inv(arr):
    n = len(arr)
    # Return back the array with inversion_count=0 if size is 0 or 1
    if(n==0 or n==1):
        return (0, arr)
    
    # Get the inversion_count of left subarray with merge_sort approach
    INV_1, sorted_arr_1 = count_inv(arr[:n//2])
    # Get the inversion_count of right subarray with merge_sort approach
    INV_2, sorted_arr_2 = count_inv(arr[n//2:])
    # Get the inversion_count for merging
    INV_MERGE, sorted_arr = count_inv_merge(sorted_arr_1, sorted_arr_2)

    return (INV_1+INV_2+INV_MERGE, sorted_arr)


def count_inv_merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    count = 0
    result = []
    i=0; j=0
    while(i<n1 and j<n2):
        if(arr1[i] <= arr2[j]):
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            # Jab bhi right subarray(arr2) ka koi element pick hota hai that means
            # It is smaller than all the elements to the right of i till n1 of left subarray(arr1)
            # and wo in saare elements ke liye inversions dega. So  count += n1-i
            count+= n1-i
            j+=1
    
    if(i<n1):
        result += arr1[i:]
    
    if(j<n2):
        result += arr2[j:]

    return (count, result)



print("Example-1: count_inv(arr)" )
arr = [2, 4, 1, 3, 5]
print(count_inv(arr)[0])


print("Example-2: count_inv(arr)" )
arr = [1, 20, 6, 4, 5]
print(count_inv(arr)[0])
