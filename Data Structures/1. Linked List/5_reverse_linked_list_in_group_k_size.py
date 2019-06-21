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
    
    
    def reverse_in_group_of_size(self, k):
        # Take prev as None, start the current_node from first node and take an empty stack to store atmost k items.
        prev = None
        current_node = self.head
        stack = []
        
        # Till the current_node is not None.
        while(current_node):
            count = 0
            # Take at most k elements in stack and keep moving the current_node.
            while(count<k and current_node):
                stack.append(current_node.data)
                current_node = current_node.next
                count += 1
            
            # After k nodes are pushed to stack current will point to k+1 the node but prev will still be unchanged.
            # Now start popping from stack and make new_node and check:
            while(stack):
                new_node = Node(stack.pop())
                # If prev is None, then set the head to point to prev (it will only happen for the first element when prev is None).
                if(prev is None):
                    self.head = new_node
                else:     # Else set next of prev as new_node
                    prev.next = new_node
                
                # Update the prev as new_node.
                prev = new_node

            

print("Linked List at Start:")
linked_list = LinkedList()
linked_list.push(8)
linked_list.push(7)
linked_list.push(6)
linked_list.push(5)
linked_list.push(4)
linked_list.push(3)
linked_list.push(2)
linked_list.push(1)
linked_list.print_list()
print("\nAfter reverse_in_group_of_size(3):")
linked_list.reverse_in_group_of_size(3)
linked_list.print_list()