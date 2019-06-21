# import
from collections import deque
  
# initialize
dq = deque([1,2,3])

print ("Current Deque: {}".format(dq))
  
# append(): Insert 4 at end
dq.append(4) 
print ("Deque after append 4 at right is: {}".format(dq))
  
# append(): Insert 6 at start
dq.appendleft(6) 
print ("Deque after append 6 at left is: {}".format(dq))
  
# pop(): Pop from end
dq.pop()
print ("Deque after pop from right is : {}".format(dq))

# popleft(): Pop from start
dq.popleft()
print ("Deque after pop from left is : {}".format(dq))

#================================================================

dq = deque([1, 2, 3, 3, 4, 2, 4])
print ("\nNew Current Deque : {}".format(dq))

# insert(): Insert 7 at 5th position 
dq.insert(4, 7)
print ("Deque after insert 7 at 5th position is : {}".format(dq))

# insert(): Occurrence of 4 b/w 2nd and 7th index.
print ("In Deque 4 first occurs at a position : {}".format(dq.index(4, 2, 7)))

# count(): Count the occurrences of 3 
print ("In Deque count of 3 : {}".format(dq.count(3)))

# remove(): Remove the first occurrence of 3 
dq.remove(3) 
print ("Deque after after Deleting first occurrence of 3 is : {}".format(dq))

#================================================================

dq = deque([1, 2, 3])
print ("\nNew Current Deque : {}".format(dq))

# extend(): To add [4, 5, 6] at right end
dq.extend([4, 5, 6]) 
print ("Deque after extend deque at end is : {}".format(dq))
  
# extendleft(): adds 7,8,9 at left end
dq.extendleft([7,8,9]) 
print ("Deque after extend deque start : {}".format(dq))
  
# rotate(): rotates by 3 to right
dq.rotate(3) 
print ("Deque after rotate right by 3 : {}".format(dq))

# rotate(): rotates by 3 to left 
dq.rotate(-3) 
print ("Deque after rotate left by 3 : {}".format(dq))
  
# reverse(): reverse the deque 
dq.reverse()
print ("Deque after reversed : {}".format(dq))