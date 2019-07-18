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
    
    
    def reverse(self):
        # Take prev_node as None and current_node as first node.
        prev_node = None
        current_node = self.head

        # While current_node doesn't become None keep going:
        while(current_node):
            # Take the next_node as next of current_node.
            next_node = current_node.next
            # Make the next of current_node point to prev_node
            current_node.next = prev_node
            # Update the prev_node as current_node and current_node as next_node
            prev_node = current_node
            current_node = next_node
        
        # Make head point to prev_node which was the last node and now in reverse it becomes first.
        self.head = prev_node

        

print("Linked List at Start:")
linked_list = LinkedList()
linked_list.push(5)
linked_list.push(3)
linked_list.push(6)
linked_list.push(7)
linked_list.push(4)
linked_list.print_list()
print("\nAfter reverse():")
linked_list.reverse()
linked_list.print_list()
