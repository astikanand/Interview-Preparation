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
    
    if(result):
        print("Yes")
    else:
        print("No")




print("Example-1: check_2_line_segments_intersection([(1,1), (10,1)], [(1,2), (10,2)])")
check_2_line_segments_intersection([(1,1), (10,1)], [(1,2), (10,2)])

print("\nExample-2: check_2_line_segments_intersection([(10,0), (0,10)], [(0,0), (10,10)])")
check_2_line_segments_intersection([(10,0), (0,10)], [(0,0), (10,10)])

print("\nExample-3: check_2_line_segments_intersection([(-5,-5), (0,0)], [(1,1), (10,10)])")
check_2_line_segments_intersection([(-5,-5), (0,0)], [(1,1), (10,10)])
