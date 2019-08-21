def nuts_bolts_match(nuts, bolts, low, high):
    if low < high:
        # Set last character of bolts for nuts partition. 
        pivot = partition(nuts, low, high, bolts[high])

        # Now using the partition index of nuts set pivot for bolts partition
        partition(bolts, low, high, nuts[pivot])

        # Recur for [low...pivot-1] & [pivot+1...high] for nuts and bolts array. 
        nuts_bolts_match(nuts, bolts, low, pivot-1)
        nuts_bolts_match(nuts, bolts, pivot+1, high)


def partition(arr, low, high, pivot):
    i = j = low

    while(j < high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[high], arr[j] = arr[j], arr[high]
            j -= 1
        
        j += 1
    
    arr[i], arr[high] = arr[high], arr[i]

    return i            


print("Example-1: Nuts and Bolts Problem")
nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
nuts_bolts_match(nuts, bolts, 0, 5)
print(nuts)
print(bolts)
