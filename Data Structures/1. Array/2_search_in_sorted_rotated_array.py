def search(arr, start, end, key): 
    if start > end:
        print("Key {} : NOT Found".format(key))
        return
      
    mid = (start + end) // 2
    if arr[mid] == key:
        print("Key {} : Found at index {}".format(key, mid))
        return
  
    # If arr[start...mid] i.e 1st half is sorted  
    if arr[start] <= arr[mid]: 
        # As the 1st subarray is sorted, Quickly check if key lies in first half or 2nd half  
        if key >= arr[start] and key <= arr[mid]: 
            return search(arr, start, mid-1, key)
        else:
            return search(arr, mid+1, end, key) 
    # Else arr[start..mid] is not sorted, then arr[mid... end] must be sorted
    else:
        # As the 2nd subarray is sorted, Quickly check if key lies in 2nd half or first half
        if key >= arr[mid] and key <= arr[end]: 
            return search(arr, mid+1, end, key)
        else:
            return search(arr, start, mid-1, key)


print("Example-1: search([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 3)")
search([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 3)

print("\nExample-2: search([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 4)")
search([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 4)

print("\nExample-3: search([30, 40, 50, 10, 20], 0, 4, 10)")
search([30, 40, 50, 10, 20], 0, 4, 10)
