def quick_sort(arr):
    n = len(arr)

    if( n==0 or n==1):
        return arr
    
    p_index = partition(arr)
    
    # Sort the left side of array till partition_index 
    # Sort the right side of array from partition_index till the end
    # Return the combined array
    sorted_arr = quick_sort(arr[:p_index]) + [arr[p_index]] + quick_sort(arr[p_index+1:])

    return sorted_arr


def partition(arr):
    n = len(arr)
    # Select the last element as pivot
    pivot = arr[-1]
    i = 0
    for j in range(n):
        if(arr[j] <= pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    
    # Index of pivot as pivot is also considered in swap hence i-1
    return i-1


print("Example-1: quick_sort(arr)")
arr = [10, 80, 30, 90, 70, 85, 75, 95, 40, 50, 70]
print(quick_sort(arr))

print("Example-2: quick_sort(arr)")
arr = [4, 3, 2, 10, 12, 1, 5, 6]
print(quick_sort(arr))

print("Example-3: quick_sort(arr)")
arr = [12, 11, 13, 5, 6]
print(quick_sort(arr))
