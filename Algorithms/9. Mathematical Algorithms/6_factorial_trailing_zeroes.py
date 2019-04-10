def factorial_trailing_zeroes(n):
    count = 0
    k = 5
    while(n > 0):
        n = int(n/k)
        count += n
        k = k*k
    
    print(count)



print("Example-1: factorial_trailing_zeroes(5)")
factorial_trailing_zeroes(5)

print("Example-2: factorial_trailing_zeroes(20)")
factorial_trailing_zeroes(20)

print("Example-3: factorial_trailing_zeroes(100)")
factorial_trailing_zeroes(100)
