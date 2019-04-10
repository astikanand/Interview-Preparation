def count_digits_sequence_decodings(digits):
    n = len(digits)

    # base cases 
    if(n==0 or n==1):
        return 1
    
    count = 0

    # If the last digit is not 0, then last digit must add to the number of words.
    if(digits[-1]>'0'):
        count += count_digits_sequence_decodings(digits[:-1])
    
    # If the last two digits form a number smaller than or equal to 26, then consider last two digits and recur
    if(digits[-2]=='1' or (digits[-2]=='2' and digits[-1]<='6')):
        count += count_digits_sequence_decodings(digits[:-2])
    
    return count


print("Recursive Approach")
print("Example-1: count_digits_sequence_decodings('12')")
print(count_digits_sequence_decodings('12'))

print("Example-1: count_digits_sequence_decodings('121')")
print(count_digits_sequence_decodings('121'))

print("Example-3: count_digits_sequence_decodings('1234')")
print(count_digits_sequence_decodings('1234'))


# ===========================================================================================================================================


def count_digits_sequence_decodings_DP(digits):
    n = len(digits)
    count = [0]*(n+1) # A table to store results of subproblems 

    # Base cases 
    count[0] = 1;  count[1] = 1  
  
    for i in range(2, n+1):  
        count[i] = 0
  
        # If the last digit is not 0, then last digit must add to the number of words  
        if (digits[i-1] > '0'):  
            count[i] = count[i-1] 

        # If the last two digits form a number smaller than or equal to 26, then last two digits form a valid character  
        if (digits[i-2]=='1' or (digits[i-2]=='2' and digits[i-1]<='6') ):  
            count[i] += count[i-2] 
  
    return count[n]


print("\nDP Approach")
print("Example-1: count_digits_sequence_decodings_DP('12')")
print(count_digits_sequence_decodings_DP('12'))

print("Example-1: count_digits_sequence_decodings_DP('121')")
print(count_digits_sequence_decodings_DP('121'))

print("Example-3: count_digits_sequence_decodings_DP('1234')")
print(count_digits_sequence_decodings_DP('1234'))
