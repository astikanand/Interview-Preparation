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
        # Make a new_node.
        new_node = Node(data)
        # (1) Next of new_node points to node where head was poiting earlier.
        new_node.next = self.head
        # (2) Now, head points to new_node.
        self.head = new_node
    

    def append(self, data):
        # Make a new_node.
        new_node = Node(data)

        # (1) Find the last node using temp and make the next of last_node point to new_node.
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
    

    def insert_at(self, position, data):
        # If position is 0 call push to insert at front.
        if(position == 0):
            self.push(data)
            return
        
        # Now find position to insert, need to jump only position-2 coz already at 1 and need to go 1 less. 
        # (Example-1: if position=5, already at 1 so ust 3 jumps to reach 4th posittion.)
        temp = self.head
        while(temp.next and position-2 > 0):
            temp = temp.next
            position -= 1
        
        # Make new_node
        new_node = Node(data)
        # (1) Next of new_node points to next of temp.
        new_node.next = temp.next
        # (2) Next of temp points to new_node.
        temp.next = new_node
    
        

print("Linked List at Start:")
linked_list = LinkedList()
linked_list.push(7)
linked_list.push(6)
linked_list.push(1)
linked_list.push(5)
linked_list.print_list()
print("\nAfter push(3):")
linked_list.push(3)
linked_list.print_list()
print("\nAfter insert_at(4, 9):")
linked_list.insert_at(4, 9)
linked_list.print_list()
print("\nAfter append(2):")
linked_list.append(2)
linked_list.print_list()
