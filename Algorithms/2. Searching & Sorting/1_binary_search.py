def binary_search(arr, l, r, num):
    if(r>=l):
        mid = (l+r)//2
        # If mid element is equal to num, return index
        if(arr[mid]==num):
            return mid
        # If mid element is lesser than num, search in the right half of the array
        elif(arr[mid] < num):
            return binary_search(arr, mid+1, r, num)
        # If mid element is grater searhc in left half of the array
        else:
            return binary_search(arr, l, mid-1, num)
    
    return -1



print("Example-1: binary_search(arr, num)")
arr = [2, 3, 4, 10, 40]
print(binary_search(arr, 0, 4, 10))

print("Example-2: binary_search(arr, num)")
arr = [2, 3, 4, 10, 40]
print(binary_search(arr, 0, 4, 15))

print("Example-3: binary_search(arr, num)")
arr = [2]
print(binary_search(arr, 0, 0, 2))