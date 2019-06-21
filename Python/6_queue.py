# import
from queue import Queue

# Initilaize
q = Queue(maxsize=5) 
  
# put(): to enqueue data to queue
print("Enqueue 5, 9, 1, 7 to queue.")
q.put(5) ; q.put(9); q.put(1); q.put(7)

# get(): to dequeue data from queue
print("Data dequeued from queue : {}".format(q.get()))

# queue[0]: front of the queue
print("Data at front of queue : {}".format(q.queue[0]))

# queue[-1]: rear of the queue
print("Data at rear of queue : {}".format(q.queue[-1]))

# qsize(): Size of queue
print("Size of queue : {}".format(q.qsize()))

# full(): Check full
print("Is full? : {}".format(q.full()))

# empty(): Check empty
print("Is empty? : {}".format(q.empty()))
