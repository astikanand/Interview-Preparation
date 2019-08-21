def square_distance(a, b):
    return (b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1])


def check_square(p1, p2, p3, p4):
    is_square = False

    ## Calculate distances from p1
    d2 = square_distance(p1, p2) # from p1 to p2 
    d3 = square_distance(p1, p3) # from p1 to p3 
    d4 = square_distance(p1, p4) # from p1 to p4 
  
    # If lengths of (p1, p2) and (p1, p3) are same, then following conditions must meet to form a square:
    #   • 1) Square of length of (p1, p4) is same as twice the square of (p1, p2) 
    #   • 2) Square of length of (p2, p3) is same as twice the square of (p2, p4) 
  
    if (d2 == d3 and 2*d2 == d4 and 2*square_distance(p2, p4) == square_distance(p2, p3)):
        is_square = True
  
    # Cases similar to above case
    if (d3 == d4 and 2*d3 == d2 and 2*square_distance(p3, p2) == square_distance(p3, p4)):
        is_square = True

    if (d2 == d4 and 2*d2 == d3 and 2*square_distance(p2, p3) == square_distance(p2, p4)):
        is_square = True
  
    if(is_square):
        print("Square")
    else:
        print("Not Square")


print("Example-1: check_square((20, 10), (10, 20), (20, 20), (10, 10))")
check_square((20, 10), (10, 20), (20, 20), (10, 10))

print("\nExample-2: check_square((20, 10), (10, 20), (20, 20), (10, 20))")
check_square((20, 10), (10, 20), (20, 20), (10, 20))
