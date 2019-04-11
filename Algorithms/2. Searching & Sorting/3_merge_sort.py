def merge_sort(arr):
    n = len(arr)

    # Base case: if n = 0 return [] and if n = 1 return [num1]
    if(n==0 or n==1):
        return arr
    
    # Divide the array into 2 halves and call merge_sort on both
    sorted_arr1 = merge_sort(arr[:n//2])
    sorted_arr2 = merge_sort(arr[n//2:])

    # Call merge to merge both sorted_arr1 and sorted_arr2
    sorted_arr = merge(sorted_arr1, sorted_arr2)

    return sorted_arr


def merge(sorted_arr1, sorted_arr2):
    n1 = len(sorted_arr1)
    n2 = len(sorted_arr2)

    i=0; j=0
    merged_arr = []
    while(i<n1 and j<n2):
        if(sorted_arr1[i] <= sorted_arr2[j]):
            merged_arr.append(sorted_arr1[i])
            i += 1
        else:
            merged_arr.append(sorted_arr2[j])
            j += 1
    
    # If elements are left in sorted_arr1
    if(i<n1):
        merged_arr += sorted_arr1[i:]
    
    # If elements are left in sorted_arr2
    if(j<n2):
        merged_arr += sorted_arr2[j:]
    
    
    return merged_arr



print("Example-1: merge_sort(arr)")
arr = [4, 3, 2, 10, 12, 1, 5, 6]
print(merge_sort(arr))

print("Example-2: merge_sort(arr)")
arr = [12, 11, 13, 5, 6]
print(merge_sort(arr))
