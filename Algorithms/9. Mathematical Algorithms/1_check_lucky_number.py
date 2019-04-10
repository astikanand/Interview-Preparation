def check_lucky(n, k):
    # n is current_position of number
    # k represents at this iteration kth numbers will be deleted, at start k = 2

    if(n%k == 0):
        return False
    
    if(k > n):
        return True
    
    # Calculate new_position after deleting kth number, increase k
    n = n - int(n/k)
    k += 1

    return check_lucky(n, k)



print("Example-1: check_lucky : 5")
print(check_lucky(5, 2))

print("Example-2: check_lucky : 19")
print(check_lucky(19, 2))
