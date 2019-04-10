def square_root(n):
    # Here using n itself as initial approximation but this can definitely be improved
    x = n
    y = 1

    # a decides the accuracy level 
    a = 0.000001

    while(x - y > a): 
        x = (x + y)/2
        y = n / x 
      
    return x



print("Example-1: square_root : 4")
print(round(square_root(4), 5))

print("Example-2: square_root : 50")
print(round(square_root(50), 5))
