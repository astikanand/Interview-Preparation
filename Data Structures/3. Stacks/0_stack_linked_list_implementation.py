class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
    

    def is_empty(self):
        return True if self.head is None else False


    def push(self, data):
        new_stack_node = StackNode(data)
        new_stack_node.next = self.head
        self.head = new_stack_node
    

    def pop(self):
        if(self.head is None):
            return "Underflow"
        
        temp = self.head
        self.head = self.head.next
        return temp.data
    

    def top(self):
        if(self.head is None):
            return "Underflow"
        
        return self.head.data



print("Example:- Linked List Implementation of Stack.")
my_stack = Stack()
print("Push: 4, 1, 7, 8 to stack.")
my_stack.push(4)
my_stack.push(1)
my_stack.push(7)
my_stack.push(8)
print("Pop the first element: {}".format(my_stack.pop()))
print("Top element in stack: {}".format(my_stack.top()))
print("Is stack empty? {}".format(my_stack.is_empty()))