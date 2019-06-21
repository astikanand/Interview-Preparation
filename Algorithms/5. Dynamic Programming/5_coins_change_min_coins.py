import sys

def coin_change_min_coins_recursive(coins, N):
    m = len(coins)

    # if N==0, No coins needed
    if(N == 0):
        return 0
    
    # if N < 0, return MAX and also when no coins
    if(N < 0 or m == 0):
        return sys.maxsize
    
    # Now find minimum no. of coins by including every coin one by one
    min_coins = sys.maxsize
    for i in range(m):
        min_coins = min(1 + coin_change_min_coins_recursive(coins, N-coins[i]), min_coins)
    
    return min_coins

    

# print("Example-1: coin_change_min_coins_recursive(coins, N)")
# coins = [1, 5, 6, 8]
# print(coin_change_min_coins_recursive(coins, 11))

# print("Example-2: coin_change_min_coins_recursive(coins, N)")
# coins = [2, 5, 7]
# print(coin_change_min_coins_recursive(coins, 3))



def coin_change_min_coins_DP(coins, N):
    m = len(coins)
    table = [[sys.maxsize]*(N+1) for i in range(m+1)]

    # If N = 0 then coins required = 0 --- Fill first column
    for i in range(m+1):
        table[i][0] = 0
    
    # If coins = 0 then coins required = INFINITY   --- Fill first column
    # This line can be omitted, just for understanding as we have initialized with infinity
    for j in range(1, N+1):
        table[0][j] = sys.maxsize
    
    # Now fill the table
    for i in range(1, m+1):
        for j in range(1, N+1):
            if(j-coins[i-1] < 0):
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = min(1+table[i][j-coins[i-1]], table[i-1][j])
    

    return table[m][N]



print("Example-1: coin_change_min_coins_DP(coins, N)")
coins = [1, 5, 6, 8]
print(coin_change_min_coins_DP(coins, 11))
print("Example-2: coin_change_min_coins_DP(coins, N)")
coins = [2, 5, 7]
print(coin_change_min_coins_DP(coins, 3))
