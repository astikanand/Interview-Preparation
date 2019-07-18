from queue import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    

    def push(self, data):
        # (1) Put the data first to queue2
        self.queue2.put(data)

        # (2) Put all the data from queue1 to queue2
        while(not self.queue1.empty()):
            self.queue2.put(self.queue1.get())
        
        # (3) Swap the names of two queues
        self.queue1, self.queue2 = self.queue2, self.queue1
    

    def pop(self):
        if(self.queue1.empty()):
            print("Stack Underflow")
            return 
        else:
            return self.queue1.get()
    

    def top(self):
        if(self.queue1.empty()):
            print("Stack Underflow")
            return 
        else:
            return self.queue1.queue[0]
    

    def is_empty(self):
        return self.queue1.empty()

    

print("Example:- Stack Using Queues:")
my_stack = Stack()
print("Pushed: 4, 2, 1, 3 to stack.")
my_stack.push(4)
my_stack.push(2)
my_stack.push(1)
my_stack.push(3)
my_stack.push(6)
print("6 is pushed to the stack.\n")

print("Pop the first element: {}".format(my_stack.pop()))
print("Top element in stack: {}".format(my_stack.top()))
print("Is stack empty? {}".format(my_stack.is_empty()))