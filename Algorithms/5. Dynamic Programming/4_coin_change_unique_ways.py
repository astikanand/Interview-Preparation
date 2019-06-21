def coin_change_unique_ways_recursive(coins, N):
    m = len(coins)

    # If N is less than 0 then no solution exists 
    if (N < 0): 
        return 0
    
    # If N is 0 then 1 solution : Don't include any coin
    if (N == 0): 
        return 1
  
    # If no coins, no solution exist 
    if (m == 0): 
        return 0
    
    # Answer is sum of solutions (i)including first coin (ii) excluding first coin 
    return coin_change_unique_ways_recursive(coins, N-coins[0]) + coin_change_unique_ways_recursive(coins[1:], N)
    


print("Example-1: coin_change_unique_ways_recursive(coins, N)")
coins = [1, 2, 5]
print(coin_change_unique_ways_recursive(coins, 5))
print("Example-2: coin_change_unique_ways_recursive(coins, N)")
coins = [2, 5, 3, 6]
print(coin_change_unique_ways_recursive(coins, 10))



def coin_change_unique_ways_DP(coins, N):
    m = len(coins)
    table = [[0]*(N+1) for i in range(m+1)]

    # when N=0, 1 solution:- Don't include anyone --- Fill first column
    for i in range(m+1):
        table[i][0] = 1

    # When No coins or m = 0 :- No solution possible ---- Fill first row
    # Line can be omitted as table is initialized with 0, just for better understanding
    for j in range(1, N+1):
        table[0][j] = 0
    
    # Fill rest of the table
    # table[i][j] =        table[i-1][j]         +  table[i][j-coins[i-1]] 
    # table[i][j] = (Not including current coin) + (Including current coin)
    for i in range(1, m+1):
        for j in range(1, N+1):
            # Can't include current coin
            if(j-coins[i-1] < 0):
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] + table[i][j-coins[i-1]]     # Include current coin
    
    return table[m][N]



print("Example-1: coin_change_unique_ways_DP(coins, N)")
coins = [1, 2, 5]
print(coin_change_unique_ways_DP(coins, 5))
print("Example-2: coin_change_unique_ways_DP(coins, N)")
coins = [2, 5, 3, 6]
print(coin_change_unique_ways_DP(coins, 10))
