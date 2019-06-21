def fib_memoization_top_down(n, lookup):
    if(n == 0 or n == 1):
        lookup[n] = n

    if(lookup[n] is None):
        lookup[n] = fib_memoization_top_down(n-1, lookup) + fib_memoization_top_down(n-2, lookup)
    
    return lookup[n]


print("Fibonacci: DP(Top_Down/Memoization) Approach Example-1:")
print(fib_memoization_top_down(5, [None]*(6)))

print("Fibonacci: DP(Top_Down/Memoization) Approach Example-2:")
print(fib_memoization_top_down(34, [None]*(35)))



def fib_tabulation_bottom_up(n):
    table = [0]*(n+1)
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    
    return table[n]


print("Fibonacci: DP(Bottom_Up/Tabulation) Approach Example-1:")
print(fib_tabulation_bottom_up(5))

print("Fibonacci: DP(Bottom_Up/Tabulation) Approach Example-2:")
print(fib_tabulation_bottom_up(34))
