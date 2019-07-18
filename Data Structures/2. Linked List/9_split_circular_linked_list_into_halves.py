class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    

    def push(self, data):
        new_node = Node(data)
        # new_node's next will point to the previous_first_node which head was pointing earlier
        new_node.next = self.head

        # Only 1 node : self loop
        if self.head is None:  
            new_node.next = new_node
        else:
            # last_node's next will point to new_node
            last_node = self.head
            while(last_node.next != self.head): 
                last_node = last_node.next
            last_node.next = new_node 
        
        # Now the head will point to new_node
        self.head = new_node


    def print_list(self):
        temp = self.head
        while(temp.next != self.head):
            print("{}-->".format(temp.data), end="")
            temp = temp.next
        print("{}".format(temp.data))
    

    def split_into_halves(self, second_cll):
        if(self.head is None):
            return

        fast_ptr = slow_ptr = self.head
        # If Odd no. of nodes in then fast_ptr->next becomes head and 
        # if Even no. of nodes fast_ptr->next->next becomes head 
        while(fast_ptr.next!=self.head and fast_ptr.next.next!=self.head):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        #======== Making 2nd half circular ========#
        # Start of 2nd half: slow_ptr.next
        # End of 2nd half : fast_ptr (Odd no. of nodes) || fast_ptr.next (Even no. of nodes)
        if fast_ptr.next.next == self.head: 
            fast_ptr = fast_ptr.next
        second_cll.head = slow_ptr.next
        fast_ptr.next = slow_ptr.next

        #======== Making 1st half circular ========#
        # Start of 1st half: head (self.head = self.head)
        # End of 1st half : slow_ptr)
        slow_ptr.next = self.head

        
        

print("Example-1(Odd Nodes): Original Circular Linked List:")
cll = CircularLinkedList()
cll.push(5)
cll.push(4)
cll.push(3)
cll.push(2)
cll.push(1)
cll.print_list()
print("Circular Linked List after Splitting:")
second_cll = CircularLinkedList()
cll.split_into_halves(second_cll)
cll.print_list()
second_cll.print_list()

print("\nExample-2(Even Nodes): Original Circular Linked List:")
cll = CircularLinkedList()
cll.push(6)
cll.push(5)
cll.push(4)
cll.push(3)
cll.push(2)
cll.push(1)
cll.print_list()
print("Circular Linked List after Splitting")
second_cll = CircularLinkedList()
cll.split_into_halves(second_cll)
cll.print_list()
second_cll.print_list()