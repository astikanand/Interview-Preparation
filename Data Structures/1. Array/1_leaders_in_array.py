def print_leaders(arr):
    n = len(arr)
    # Righmost element is always leader
    max_from_right = arr[-1]
    leaders = [arr[-1]]

    for i in range(n-2, 0, -1):         
        if max_from_right < arr[i]:             
            max_from_right = arr[i]
            leaders.append(arr[i])
    
    print(leaders[::-1])
    
          
print("Example-1: print_leaders([16, 17, 4, 3, 5, 2])")
print_leaders([16, 17, 4, 3, 5, 2])

