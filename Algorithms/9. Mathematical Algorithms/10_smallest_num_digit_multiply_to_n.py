def smallest_num_digit_multiply_to_n(n):
    if(n<10):
        return 10+n
    
    # p is to store the digits
    p = ""
    for i in range(9, 1, -1):
        while(n%i==0):
            p += str(i)
            n = int(n/i)
    
    # If n is still grteater than 10
    if(n>10):
        return "Not Possible"
    
    # Reverse the p now.
    p = p[::-1]

    return p
            


print("Example-1: smallest_num_digit_multiply_to_n(36)")
print(smallest_num_digit_multiply_to_n(36))

print("Example-2: smallest_num_digit_multiply_to_n(100)")
print(smallest_num_digit_multiply_to_n(100))

print("Example-3: smallest_num_digit_multiply_to_n(7)")
print(smallest_num_digit_multiply_to_n(7))

print("Example-3: smallest_num_digit_multiply_to_n(13)")
print(smallest_num_digit_multiply_to_n(13))
