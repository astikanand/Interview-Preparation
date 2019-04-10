def min_number_of_platforms_required(arrivals, departures):
    n = len(arrivals)
    arrivals.sort()
    departures.sort()

    i =0; j=0; count = 0; platforms =0
    while(i<n and j<n):
        if(arrivals[i] < departures[j]):
            count += 1
            i += 1
        else:
            if(count > platforms):
                platforms = count
            count -= 1
            j += 1

    print("Minimum Number of Platforms required = {}".format(platforms))



print("Example-1:")
arrivals    = [9.00,  9.40, 9.50,  11.00, 15.00, 18.00]
departures  = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
min_number_of_platforms_required(arrivals, departures)


# Time Complexity : O(n log n) if arrivals & departures are not sorted. 
#                 : O(n) if arrivals & departures are sorted.
# Space Complexity: O(1)