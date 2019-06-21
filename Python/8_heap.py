# import
import heapq 

# a normal list
hq = [5, 7, 9, 1, 3]

# heapify(): to convert list to heap or to constrain the heap order
heapq.heapify(hq) 
  
# Created Heap
print ("The created heap is : {}".format(hq))
  
# heappush(): push 4 to heap
heapq.heappush(hq, 4) 
print ("Heap after 4 is pushed : {}".format(hq))
  
# using heappop() to pop smallest element 
print ("The popped and smallest element is : {}".format(heapq.heappop(hq)))
print ("Heap after popping : {}".format(hq))

#===========================================================================
hq1 = [5, 7, 9, 4, 3]; hq2 = [5, 7, 9, 4, 3] 
heapq.heapify(hq1); heapq.heapify(hq2)
print("\nTwo same newly created heaps: {}".format(hq1))

# heappushpop(): to push and pop items simultaneously pops 2 
print ("The popped item from 1st using heappushpop(2) is: {}".format(heapq.heappushpop(hq1, 2)))
print("1st heap now: {}".format(hq1))
  
# heapreplace(): to push and pop items simultaneously pops 3 
print ("The popped item from 2nd using heapreplace(2) is: {}".format(heapq.heapreplace(hq2, 2)))
print("2nd heap now: {}".format(hq2))

#===========================================================================
 
hq = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(hq)
print("\nNewly created heap: {}".format(hq))
  
# nlargest(): to print 3 largest numbers prints 10, 9 and 8 
print("The 3 largest numbers in list are : {}".format(heapq.nlargest(3, hq)))
  
# nsmallest(): to print 3 smallest numbers prints 1, 3 and 4 
print("The 3 smallest numbers in list are : {}".format(heapq.nsmallest(3, hq)))