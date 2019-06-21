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
    

    def delete(self, data):
        temp = self.head

        # Check if first node is the node to be deleted if it is point the head to next of temp and make temp None.
        if(temp and temp.data == data):
            self.head = temp.next
            temp = None
            return
        
        # Search for the node to be deleted using the given data in the nodes using temp and keep prev in store.
        while(temp):
            if(temp.data == data):
                break
            prev = temp
            temp = temp.next
        
        # Point the next of prev to the next of temp and make temp None if temp exists else element not present.
        if(temp):
            prev.next = temp.next
            temp = None
        else:
            print("Element {} not present in list.".format(data))
    
      

print("Linked List at Start:")
linked_list = LinkedList()
linked_list.push(5)
linked_list.push(3)
linked_list.push(6)
linked_list.push(7)
linked_list.push(4)
linked_list.print_list()
print("\nAfter delete(6):")
linked_list.delete(6)
linked_list.print_list()
print("\nAfter delete(4):")
linked_list.delete(4)
linked_list.print_list()
print("\nAfter delete(2):")
linked_list.delete(2)
linked_list.print_list()
