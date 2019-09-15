class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def print_list(self):
        temp = self.head
        while(temp):
            print("{}-->".format(temp.data), end="")
            temp = temp.next
        print("Null")


    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    

    def detect_and_remove_loop(self):
        # If only 0 nodes or 1 node and that too  has no self.loop then cycle doesn’t exist.
        if(self.head is None or self.head.next is None):
            print("Cycle doesn't exist!")
            return
        
        # Initialize fast and slow pointers
        slow_ptr = fast_ptr = self.head
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        # Detecting the Loop
        while(slow_ptr and fast_ptr and fast_ptr.next):
            if(slow_ptr == fast_ptr):
                # Loop detected start removing the loop using fast_ptr and slow_ptr at same speed 
                # and starting slow_ptr from head and fast_ptr from meet point
                slow_ptr =  self.head
                while(slow_ptr.next != fast_ptr.next):
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next
                
                print("Cycle exists from Node-{} to Node-{}!".format(fast_ptr.data, fast_ptr.next.data))
                # Make next of fast_ptr None to break loop 
                fast_ptr.next = None
                return
            
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # If reaches here mean cycle not exists
        print("Cycle doesn't exist!")
        


print("Detect and Remove Loop Example-1:")
linked_list = LinkedList() 
linked_list.head = Node(1) 
linked_list.head.next = Node(2) 
linked_list.head.next.next = Node(3) 
linked_list.head.next.next.next = Node(4) 
linked_list.head.next.next.next.next = Node(5) 
#Create a loop for testing 
linked_list.head.next.next.next.next.next =  linked_list.head.next
linked_list.detect_and_remove_loop() 
print ("After removing loop:")
linked_list.print_list()

print("\nDetect and Remove Loop Example-2:")
linked_list = LinkedList()
linked_list.push(5)
linked_list.push(3)
linked_list.push(6)
linked_list.push(7)
linked_list.push(4)
linked_list.detect_and_remove_loop()
