import sys


def orientation(a, b, c):
    val = (b[1]-a[1])*(c[0]-b[0]) - (b[0]-a[0])*(c[1]-b[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1


def on_segment(a, b, c):
    if (b[0] <= max(a[0], c[0]) and b[0] >= min(a[0], c[0]) and
        b[1] <= max(a[1], c[1]) and b[1] >= min(a[1], c[1])): 
        return True 
  
    return False


def check_2_line_segments_intersection(line1, line2):
    p1 = line1[0]; q1 = line1[1]
    p2 = line2[0]; q2 = line2[1]

    # All 4 different orientation
    #   • p1, q1, p2 = o1 and p1, q1, q2 = o2 --> Should be different
    #   • p2, q2, p1 = o3 and p2, q2, q1 = o4 --> Should be different
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    result = False

    ### General Case 
    if o1 != o2 and o3 != o4: 
        result = True

    ### Case-2: Special Cases 
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1 
    if o1 == 0 and on_segment(p1, p2, q1):
        result = True
  
    # p1, q1 and q2 are collinear and q2 lies on segment p1q1 
    if o2 == 0 and on_segment(p1, q2, q1):
        result = True
  
    # p2, q2 and p1 are collinear and p1 lies on segment p2q2 
    if o3 == 0 and on_segment(p2, p1, q2):
        result = True
  
    # p2, q2 and q1 are collinear and q1 lies on segment p2q2 
    if o4 == 0 and on_segment(p2, q1, q2):
        result = True
    
    return result


def check_point_inside_polygon(polygon, p):
    n = len(polygon)
    # Not a polynomial
    if n < 3:
        print("Outside")
        return
    
    # Extreme point will have x as "infinity" and y same as point p
    extreme = (sys.maxsize, p[1])

    # Count for counting intersections
    count = 0

    result = False
    for i in range(n):
        current_vertex = polygon[i]
        next_vertex = polygon[(i+1)%n]

        # Check if the line segment from 'p' to 'extreme' intersects 
        # with the line segment polygon's current_vertex to next_vertex
        if check_2_line_segments_intersection((current_vertex,next_vertex), (p,extreme)):
            # If the point 'p' is collinear with line segment current_vertex---next_vertex
            # Check if it lies on segment return true if it lies, otherwise false
            if (orientation(current_vertex, p, next_vertex) == 0) :
                result = on_segment(current_vertex, p, next_vertex)
                count = 0
                break
            
            count += 1
    
    if(result or count%2 == 1):
        print("Inside")
    else:
        print("Outside")



polygon1 = [(0, 0), (10, 0), (10, 10), (0, 10)]
polygon2 = [(0, 0), (5, 5), (5, 0)]
print("Example-1: check_point_inside_polygon(polygon1, (20, 20))")
check_point_inside_polygon(polygon1, (20, 20))

print("\nExample-2: check_point_inside_polygon(polygon1, (5, 5))")
check_point_inside_polygon(polygon1, (5, 5))

print("\nExample-3: check_point_inside_polygon(polygon1, (-1, 10))")
check_point_inside_polygon(polygon1, (-1, 10))

print("\nExample-4: check_point_inside_polygon(polygon2, (3, 3))")
check_point_inside_polygon(polygon2, (3, 3))

print("\nExample-5: check_point_inside_polygon(polygon2, (5, 1))")
check_point_inside_polygon(polygon2, (5, 1))

print("\nExample-6: check_point_inside_polygon(polygon2, (8, 1))")
check_point_inside_polygon(polygon2, (8, 1))
