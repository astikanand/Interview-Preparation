def activity_selection(start, finish):
    activities = []
    n = len(start)
    for i in range(n):
        activities.append((start[i], finish[i]))
    
    # Sort the activities by finish time in increasing order and if finish times same then start time in decreasing order
    activities.sort(key=lambda k: (k[1], -k[0]))

    print("Selected Activities:")
    prev_finish = 0
    for current_start, current_finish in activities:
        if(current_start >= prev_finish):
            print("({}, {})".format(current_start, current_finish))
            prev_finish = current_finish



print("Example-1:")
start =  [10, 12, 20] 
finish = [20, 25, 30] 
activity_selection(start, finish)

print("\nExample-2:")
start =  [3 , 0 , 5 , 8 , 5, 1] 
finish = [4 , 6 , 9 , 9 , 7, 2] 
activity_selection(start, finish)


# Time Complexity : O(n log n) if input activities not sorted. 
#                 : O(n) if input activities are sorted.
# Space Complexity: O(n) :-> Creating a new array but can be done in O(1)