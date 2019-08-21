def quick_sort(arr):
    n = len(arr)

    if(n==0 or n==1):
        return arr
    
    p_index = partition(arr, n-1)

    sorted_arr = quick_sort(arr[:p_index]) + [arr[p_index]] + quick_sort(arr[p_index+1:])

    return sorted_arr


def partition(arr, end):
    pivot = arr[end]
    low = 0
    high = end-1
 
    while True:
        while (low <= high and arr[low] <= pivot):
            low += 1

        while (low <= high and arr[high] >= pivot):
            high -= 1
 
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            arr[end], arr[low] = arr[low], arr[end]
            break

    return low
    


print("Example-1: quick_sort([10, 80, 30, 90, 70, 85, 75, 95, 40, 50, 70])")
print(quick_sort([10, 80, 30, 90, 70, 85, 75, 95, 40, 50, 70]))

print("\nExample-2: quick_sort([4, 3, 2, 10, 12, 1, 5, 6])")
print(quick_sort([4, 3, 2, 10, 12, 1, 5, 6]))

print("\nExample-3: quick_sort([12, 11, 13, 5, 6])")
print(quick_sort([12, 11, 13, 5, 6]))
