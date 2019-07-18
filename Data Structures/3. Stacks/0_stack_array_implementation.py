class Stack:
    def __init__(self):
        self.stack = []
    

    def is_empty(self):
        return len(self.stack) == 0

    
    def push(self, data):
        self.stack.append(data)
    

    def pop(self):
        if(self.is_empty()):
            return "Underflow"
        return self.stack.pop()
    

    def top(self):
        if(self.is_empty()):
            return "Underflow"
        return self.stack[-1]



print("Example:- Array Implementation of Stack.")
my_stack = Stack()
print("Push: 4, 1, 7, 8 to stack.")
my_stack.push(4)
my_stack.push(1)
my_stack.push(7)
my_stack.push(8)
print("Pop the first element: {}".format(my_stack.pop()))
print("Top element in stack: {}".format(my_stack.top()))
print("Is stack empty? {}".format(my_stack.is_empty()))
