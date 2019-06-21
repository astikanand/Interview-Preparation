def count_tiling_ways(N):
    # If N <= 0 No way to put any tile
    if(N <= 0):
        return 0
    
    # If N == 1  :- only 1 way put horizontal
    # If N == 2  :- 2 ways either both horizontal or both vertical
    if (N == 1 or N == 2):
        return N
    
    # Else return no. of ways of filling board by first putting 1 tile vertically or 2 tile horizontally
    return count_tiling_ways(N-1) + count_tiling_ways(N-2)



print("Example-1: count_tiling_ways(3)")
print(count_tiling_ways(3))
print("Example-2: count_tiling_ways(4)")
print(count_tiling_ways(4))
