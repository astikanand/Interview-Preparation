# def is_subset_sum_recursive(given_set, n, given_sum):
#     if(given_sum==0):
#         return True
    
#     if(n==0 and given_sum != 0):
#         return False
    
#     return is_subset_sum_recursive(given_set, n-1, given_sum) or is_subset_sum_recursive(given_set, n-1, given_sum-given_set[n-1])


# print("Example-1: is_subset_sum_recursive(given_set, n, given_sum)")
# given_set = [1, 3, 9, 2] 
# print(is_subset_sum_recursive(given_set, 4, 5))

# print("Example-2: is_subset_sum_recursive(given_set, n, given_sum)")
# given_set = [3, 34, 4, 12, 5, 2] 
# print(is_subset_sum_recursive(given_set, 6, 11))

# print("Example-3: is_subset_sum_recursive(given_set, n, given_sum)")
# given_set = [3, 34, 4, 12, 5, 2] 
# print(is_subset_sum_recursive(given_set, 6, 13))



def is_subset_sum_dp(given_set, n, given_sum):
    table = [[False]*(given_sum+1) for i in range(n+1)]

    # Sum = 0 can be achieved by any subset by taking an empty set
    for i in range(n+1):
        table[i][0] = True
    
    # With empty set all the sum will be False except sum=0
    for i in range(1, given_sum+1):
        table[0][i] = False
    
    # Now fill the rest of table 
    for i in range(1, n+1):
        for j in range(1, given_sum+1):
            # If earlier (before adding this number in set) sum was possible, the now also it will be possible
            if(table[i-1][j] == True):
                table[i][j] = True
            # If earlier not possible check if current_sum-current_number was possible earlier, if it was then we are done.
            elif(j-given_set[i-1]>=0 and table[i-1][j-given_set[i-1]] == True):
                table[i][j] = True
            # If above 2 cases is not there, then False
            else:
                table[i][j] = False
    
    return table[n][given_sum]


print("Example-1: is_subset_sum_dp(given_set, n, given_sum)")
given_set = [1, 3, 9, 2] 
print(is_subset_sum_dp(given_set, 4, 5))

print("Example-2: is_subset_sum_dp(given_set, n, given_sum)")
given_set = [3, 34, 4, 12, 5, 2] 
print(is_subset_sum_dp(given_set, 6, 11))

print("Example-3: is_subset_sum_dp(given_set, n, given_sum)")
given_set = [3, 34, 4, 12, 5, 2] 
print(is_subset_sum_dp(given_set, 6, 13))
