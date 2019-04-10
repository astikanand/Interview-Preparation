def sieve_of_eratosthenes(n):
    primes = [True]*(n+1)
    p = 2

    # Initialize all to be True, a value in prime[i] will finally be False if i is Not a prime, else True.
    while(p*p <= n):
        # If prime[p] is still True, then it is a prime 
        if(primes[p] == True):
            # Update all multiples of p staring from p*p, then p*(p+1), p*(p+2) and so on
            for i in range(p*p, n+1, p):
                primes[i] = False
        
        p += 1
    
    # Print all primes
    for i in range(2, n+1):
        if(primes[i]):
            print(i, end=" ")
    print()



print("Example-1: sieve_of_eratosthenes : 30")
sieve_of_eratosthenes(30)

print("\nExample-2: sieve_of_eratosthenes : 101")
sieve_of_eratosthenes(101)
