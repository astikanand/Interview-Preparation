def triangle_area(x1, y1, x2, y2, x3, y3):
   return abs(0.5*(x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))) 


def point_lies_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    # Calculate Areas
    area_ABC = triangle_area(x1, y1, x2, y2, x3, y3)
    area_PAB = triangle_area(x, y, x1, y1, x2, y2)
    area_PAC = triangle_area(x, y, x1, y1, x3, y3)
    area_PBC = triangle_area(x, y, x2, y2, x3, y3)

    if(area_ABC == area_PAB + area_PAC + area_PBC):
        print("Inside")
    else:
        print("Outside")



print("Example-1: point_lies_inside_triangle(0, 0, 10, 30, 20, 0, 10, 15)")
point_lies_inside_triangle(0, 0, 10, 30, 20, 0, 10, 15)

print("\nExample-2: point_lies_inside_triangle(0, 0, 10, 30, 20, 0, 18, 25)")
point_lies_inside_triangle(0, 0, 10, 30, 20, 0, 15, 25)