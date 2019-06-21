class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def list_length(self):
        temp = self.head
        length = 0
        while(temp):
            length += 1
            temp = temp.next
        return length


    def print_list(self):
        n = self.list_length()
        temp = self.head
        print('''+---+---+    '''*n)

        while(temp):
            print("| {} | •-|--->".format(temp.data), end="")
            temp = temp.next
        print("Null")

        print('''+---+---+    '''*n)


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        

print("Linked List:")
linked_list = LinkedList()
linked_list.push(5)
linked_list.push(2)
linked_list.push(7)
linked_list.push(4)
linked_list.print_list()
