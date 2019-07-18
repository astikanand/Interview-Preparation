def first_circular_tour_visiting_all_pumps(pumps):
    n = len(pumps) 
    # Consider first petrol pump as starting point 
    start = 0 
    end = 1 
      
    curr_petrol = pumps[start][0] - pumps[start][1]
      
    # Run a loop while all petrol pumps are not visited
    while(end != start): 
        # While curr_petrol is < 0, dequeue till it become positive.  
        while(curr_petrol<0 and start!=end): 
            # Remove starting petrol pump. Change start 
            curr_petrol -= pumps[start][0] - pumps[start][1]
            start = (start +1)%n 
              
            # If 0 is being considered as start again, then there is no possible solution 
            if start == 0: 
                return -1
  
        # Add a petrol pump to current tour 
        curr_petrol += pumps[end][0] - pumps[end][1] 
        end = (end +1) % n 
  
    return start+1  



print("Example-1: first_circular_tour_visiting_all_pumps()")
pumps = [(4, 6), (6, 5), (7, 3), (4, 5)]
print(first_circular_tour_visiting_all_pumps(pumps))

print("Example-2: first_circular_tour_visiting_all_pumps()")
pumps = [(4, 6), (6, 5), (3, 5), (10, 5)]
print(first_circular_tour_visiting_all_pumps(pumps))