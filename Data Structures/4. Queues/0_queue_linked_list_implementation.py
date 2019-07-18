class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
    

    def is_empty(self):
        return True if self.head is None else False


    def enqueue(self, data):
        new_queue_node = QueueNode(data)
        new_queue_node.next = self.head
        self.head = new_queue_node
    

    def dequeue(self):
        if(self.is_empty()):
            return "Empty Queue"
        
        if(self.head.next is None):
            dequeued_data = self.head.data
            self.head = None
            return dequeued_data
        
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        
        dequeued_data = temp.next.data
        temp.next = None
        return dequeued_data
    

    def front(self):
        if(self.is_empty()):
            return "Empty Queue"

        temp = self.head
        while(temp.next):
            temp = temp.next
        
        return temp.data
    

    def rear(self):
        if(self.is_empty()):
            return "Empty Queue"
        return self.head.data



print("Example:- LinkedList Implementation of Queue.")
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
