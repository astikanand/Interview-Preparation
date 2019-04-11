def power(k, n):
    if(n==0):
        return 1
    
    temp = power(k, n//2)
    if(n%2==0):
        return temp*temp
    else:
        return k*temp*temp



print("Example-1: power(2, 3)")
print(power(2, 3))

print("Example-2: power(7, 9)")
print(power(7, 9))
