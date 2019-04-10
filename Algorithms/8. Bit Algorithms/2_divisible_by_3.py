def is_divisible_by_3(n):
    # Make n positive coz if +n is divisible by 3 then -n is also divisible.
    n = abs(n)

    if(n == 0):
        return True
    
    if(n == 1):
        return False
    
    odd_count = 0; even_count = 0
    while(n):
        # If odd bit is set then increment odd counter 
        if(n & 1):
            odd_count += 1
        n = n >> 1

        # If even bit is set then increment even counter
        if(n & 1):
            even_count += 1
        n = n >> 1
    
    return is_divisible_by_3(abs(odd_count-even_count))



print("Example-1: is_divisible_by_3(23)")
print(is_divisible_by_3(23))

print("Example-2: is_divisible_by_3(111)")
print(is_divisible_by_3(111))
