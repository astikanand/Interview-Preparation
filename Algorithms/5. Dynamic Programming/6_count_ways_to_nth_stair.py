def count_ways_to_nth_stair(N):
    # If N <= 0 :- 0 or less stairs no ways to reach Nth stair
    if(N <= 0):
        return 0
    
    # If N == 1  :- only 1 way walk 1 stair
    # If N == 2  :- 2 ways ({1,1}, {2})
    if (N == 1 or N == 2):
        return N
    
    # Else return no. of ways of reaching Nth stair by taking 1 step and 2 steps at once
    return count_ways_to_nth_stair(N-1) + count_ways_to_nth_stair(N-2)



print("Example-1: count_ways_to_nth_stair(3)")
print(count_ways_to_nth_stair(3))
print("Example-2: count_ways_to_nth_stair(4)")
print(count_ways_to_nth_stair(4))
