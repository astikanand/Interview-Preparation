def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        key = arr[i]

        # Now find a place to insert this key by shifting every left element which is larger to right by 1
        # Here we are using linear search to find a place to insert key in sorted arr till i-1
        # We can also use binary search to find that particular place :--> Binary Insertion Sort
        j = i-1
        while(j>=0 and arr[j]> key):
            arr[j+1] = arr[j]
            j -= 1
        
        # arr[j] is smaller than or equal to key, so insert key after it
        arr[j+1] = key
    
    return arr



print("Example-1: insertion_sort(arr)")
arr = [4, 3, 2, 10, 12, 1, 5, 6]
print(insertion_sort(arr))

print("Example-2: insertion_sort(arr)")
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
