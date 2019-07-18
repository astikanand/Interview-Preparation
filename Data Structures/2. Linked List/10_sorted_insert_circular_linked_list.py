class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    

    def sorted_insert(self, data):
        current_node = self.head
        new_node = Node(data)

        #### Case-1: If this is first node being inserted make the self loop.
        if current_node is None:
            # (1) Make the next of new_node point to new_node itself (self-loop).
            new_node.next = new_node
            # (2) Point the head to new_node.
            self.head = new_node
        
        #### Case-2: Insert at starting before head.
        elif(data <= current_node.data):
            # (1) Make the next of new_node point to where head was pointing earlier.
            new_node.next = self.head

            # (2) Find the last node and make last_node's next point to new_node.
            last_node = self.head
            while(last_node.next != self.head): 
                last_node = last_node.next
            last_node.next = new_node

            # (3) Point the head to new_node.
            self.head = new_node
        
        #### Case-3: Insert by searching (linear search) the appropriate place to insert.
        else:
            while( current_node.next != self.head and data > current_node.next.data):
                current_node = current_node.next
            
            # (1) Make the next of new_node point to where current was pointing earlier (current.next).
            new_node.next = current_node.next
            # (2) Make the next of current_node point to new_node.
            current_node.next = new_node



    def print_list(self):
        temp = self.head
        while(temp.next != self.head):
            print("{}-->".format(temp.data), end="")
            temp = temp.next
        print("{}-->{}".format(temp.data, temp.next.data))
    


print("Original Circular Linked List:")
cll = CircularLinkedList()
cll.sorted_insert(4)
cll.sorted_insert(2)
cll.sorted_insert(8)
cll.sorted_insert(7)
cll.print_list()
print("\nInsertion at Beginning (1):")
cll.sorted_insert(1)
cll.print_list()
print("\nInsertion in Between (5):")
cll.sorted_insert(5)
cll.print_list()
print("\nInsertion at Last(9):")
cll.sorted_insert(9)
cll.print_list()