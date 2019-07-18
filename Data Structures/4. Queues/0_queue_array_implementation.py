class Queue: 
    def __init__(self): 
        self.queue = []


    def is_empty(self):
        return len(self.queue) == 0
    

    def enqueue(self, data):
        self.queue.append(data)
    

    def dequeue(self):
        if(self.is_empty()):
            return "Empty Queue"
        return self.queue.pop()
    

    def front(self):
        if(self.is_empty()):
            return "Empty Queue"
        return self.queue[0]
    

    def rear(self):
        if(self.is_empty()):
            return "Empty Queue"
        return self.queue[-1]
  

print("Example:- Array Implementation of Queue.")
my_queue = Queue()
print("Enqueue: 10, 20, 30, 40 to queue.")
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
print("Dequeue the first element: {}".format(my_queue.dequeue()))
print("Front element in queue: {}".format(my_queue.front()))
print("Rear element in queue: {}".format(my_queue.rear()))
print("Is queue empty? {}".format(my_queue.is_empty()))
