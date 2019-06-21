from queue import LifoQueue

class Queue:
    def __init__(self):
        self.stack1 = LifoQueue()
        self.stack2 = LifoQueue()
    

    def enqueue(self, data):
        # (1) Put all the data first to stack2
        while(not self.stack1.empty()):
            self.stack2.put(self.stack1.get())

        # (2) Put the current data also to stack2
        self.stack2.put(data)
        
        # (3) Move evrything back to stack1 from stack2
        while(not self.stack2.empty()):
            self.stack1.put(self.stack2.get())
    

    def dequeue(self):
        if(self.stack1.empty()):
            print("Empty Queue")
            return 
        else:
            return self.stack1.get()
    

    def front(self):
        if(self.stack1.empty()):
            print("Empty Queue")
            return 
        else:
            return self.stack1.queue[-1]
    

    def rear(self):
        if(self.stack1.empty()):
            print("Empty Queue")
            return 
        else:
            return self.stack1.queue[0]
    

    def is_empty(self):
        return self.stack1.empty()

    

print("Example:- Queue Using Stacks:")
my_queue = Queue()
print("Enqueue: 3, 1, 2, 4 to queue.")
my_queue.enqueue(3)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(6)

print("6 is enqueued to the queue.\n")
print("Dequeue the element: {}".format(my_queue.dequeue()))
print("Front element in queue: {}".format(my_queue.front()))
print("Rear element in queue: {}".format(my_queue.rear()))
print("Is queue empty? {}".format(my_queue.is_empty()))