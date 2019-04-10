import math

def prime_factors(n):
    # Check 2 as prime factors
    while(n%2 == 0):
        print(2, end=" ")
        n = int(n/2)
    
    # Check 3, 5, 7, 11, ... and so on as prime factors
    for i in range(3, int(math.sqrt(n))+1, 2):
        while(n%i==0):
            print(i, end=" ")
            n = int(n/i)
    

    # If n is a prime greater than 2
    if(n > 2):
        print(n)
    
    print()


print("Example-1: prime_factors(12)")
prime_factors(12)

print("Example-2: prime_factors(315)")
prime_factors(315)
