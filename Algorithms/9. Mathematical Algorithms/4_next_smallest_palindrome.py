import math


def reverse(string):
    return string[::-1]


def all_9s(n):
    for digit in n:
        if(digit != "9"):
            return False
    return True


def next_smallest_palindrome(n):
    n = str(n)
    k = len(n)
    # If all digits are 9s then put 1(k-1 zeroes)1
    if(all_9s(n)):
        return "1"+str("0"*(k-1))+"1"
    
    # Get the left half
    left_half = n[:(int(math.ceil(k/2)))]
    # If the number of digits are even
    if(k%2==0):
        # Check if created palindrome i.e. pal = left_half + reverse(left_half) is lesser or equal to given number
        # If it is lesser or equal increment left_half by 1.
        if(left_half + reverse(left_half) <= n):
            left_half = str(int(left_half)+1)
        
        pal = left_half + reverse(left_half)
    # If number of digits are odd
    else:
        if(left_half + reverse(left_half[:-1]) <= n):
            left_half = str(int(left_half)+1)
        
        pal = left_half + reverse(left_half[:-1])

    return pal


print("Example-1: next_smallest_palindrome(999)")
print(next_smallest_palindrome(999))

print("Example-2: next_smallest_palindrome(1234)")
print(next_smallest_palindrome(1234))

print("Example-3: next_smallest_palindrome(1213)")
print(next_smallest_palindrome(1213))

print("Example-4: next_smallest_palindrome(1221)")
print(next_smallest_palindrome(1221))

print("Example-5: next_smallest_palindrome(23921)")
print(next_smallest_palindrome(23921))

print("Example-6: next_smallest_palindrome(23941)")
print(next_smallest_palindrome(23941))
