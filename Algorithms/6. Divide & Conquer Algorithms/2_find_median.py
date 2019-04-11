def median(arr):
    n = len(arr)
    if(n%2==0):
        return (arr[(n//2)-1] + arr[n//2])/2
    else:
        return arr[n//2]


def find_median(arr1, arr2):
    n = len(arr1)

    if(n==0):
        return -1
    # 1 element in each: Median = (arr1[0] + arr2[0])/2
    elif(n==1):
        return (arr1[0] + arr2[0])/2
    # 2 elements in each: Median = (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1]))/2
    elif(n==2):
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1]))/2
    else:
        # Median of the 2 arrays for comparison
        M1 = median(arr1)
        M2 = median(arr2)

        # We are done return median
        if(M1 == M2):
            return M1
        # As M1>M2 so, median should lie b/w arr1[.....M1] and arr2[M2......]
        elif(M1>M2):
            if(n%2==0):
                return find_median(arr1[:n//2], arr2[n//2:])
            else:
                return find_median(arr1[:n//2+1], arr2[n//2:])
        # M1<M2 so, median should lie b/w arr1[M1.....] and arr2[.....M2]
        else:
            if(n%2==0):
                return find_median(arr1[n//2:], arr2[:n//2])
            else:
                return find_median(arr1[n//2:], arr2[:n//2+1])



print("Example-1: find_median(arr1, arr2)")
arr1 = [1, 2, 3, 6] 
arr2 = [4, 6, 8, 10]
print(find_median(arr1, arr2))

print("Example-2: find_median(arr1, arr2)")
arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]
print(find_median(arr1, arr2))
