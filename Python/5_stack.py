# import
from queue import LifoQueue

# Initilaize
s = LifoQueue(maxsize=5) 
  
# put(): to psuh data to stack
print("Push 5, 9, 1, 7 to stack.")
s.put(5) ; s.put(9); s.put(1); s.put(7)

# get(): to pop data from stack
print("Data popped from stack : {}".format(s.get()))

# queue[-1]: top of the stack
print("Data at top of stack : {}".format(s.queue[-1]))

# qsize(): Size of stack
print("Size of stack : {}".format(s.qsize()))

# full(): Check full
print("Is full? : {}".format(s.full()))

# empty(): Check empty
print("Is empty? : {}".format(s.empty()))
