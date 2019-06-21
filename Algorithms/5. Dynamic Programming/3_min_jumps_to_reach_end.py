import sys

def min_jump_to_reach_end_recursive(arr, start, end):
    # Base case: when start position and end position are same 
    if (start == end): 
        return 0
  
    # When nothing is reachable from the given position
    if (arr[start] == 0): 
        return sys.maxsize 
  
    # Just check where you can reach from start and then call min_jump from there
    min_jumps = sys.maxsize 
    for i in range(1, arr[start]+1):
        next_start = start+i
        if(next_start < n): 
            jumps = 1 + min_jump_to_reach_end_recursive(arr, next_start, end) 
            if (jumps < min_jumps): 
                min_jumps = jumps
  
    return min_jumps
    



print("Min Jump Recursive Example-1: min_jump_to_reach_end_recursive(arr, start, end)")
arr = [2, 3, 1, 2, 3, 4, 2, 0, 8, 1] 
n = len(arr) 
jumps = min_jump_to_reach_end_recursive(arr, 0, n-1)
if(jumps == sys.maxsize):
    print("Unreachable")
else: 
    print("Jumps: {}".format(jumps))

print("\nMin Jump Recursive Example-2: min_jump_to_reach_end_recursive(arr, start, end)")
arr = [2, 3, 1, 2, 3, 2, 1, 0, 8, 1] 
n = len(arr) 
jumps = min_jump_to_reach_end_recursive(arr, 0, n-1)
if(jumps == sys.maxsize):
    print("Unreachable")
else: 
    print("Jumps: {}".format(jumps))




def min_jump_to_reach_end_DP(arr):
    n = len(arr)
    # Initialize jumps_required as "infinity" for every element
    jumps_required = [sys.maxsize]*n
    actual_jump = [0]*n

    # First element is reachable by 0 jumps
    jumps_required[0] = 0

    for i in range(1, n):
        for j in range(i):
            # Check if from j we can reach i or not??
            # If j + arr[j] >= i : then we can reach i
            if(j+arr[j] >= i):
                # If i is reachable from j in lesser jumps than earlier update the jumps to reach i
                # Update the actual jump table also
                if(jumps_required[j]+1 < jumps_required[i]):
                    jumps_required[i] = jumps_required[j]+1
                    actual_jump[i] = j
    
    # Now print number of jumps and actual jump
    if(jumps_required[n-1] == sys.maxsize):
        print("Unreachable")
    else:
        print("Jumps: {}".format(jumps_required[n-1]))
        k = n-1
        print("Actual Jumps: end", end="")
        while(k>0):
            print("<--{}".format(actual_jump[k]), end="")
            k = actual_jump[k]
        print()



print("Min Jump DP Example-1: min_jump_to_reach_end_DP(arr)")
arr = [2, 3, 1, 2, 3, 4, 2, 0, 8, 1] 
jumps = min_jump_to_reach_end_DP(arr)

print("\nMin Jump DP Example-2: min_jump_to_reach_end_DP(arr)")
arr = [2, 3, 1, 2, 3, 2, 1, 0, 8, 1] 
jumps = min_jump_to_reach_end_DP(arr)
