class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    

    def push(self, data):
        current_node = self.head
        new_node = Node(data)

        #### Case-1: If this is first node being inserted make the self loop.
        if current_node is None:
            # (1) Make the next of new_node point to new_node itself (self-loop).
            new_node.next = new_node
            # (2) Point the head to new_node.
            self.head = new_node
        #### Case-2: Insert at starting before head.
        else:
            # (1) Make the next of new_node point to where head was pointing earlier.
            new_node.next = self.head
            # (2) Find the last node and make last_node's next point to new_node.
            last_node = self.head
            while(last_node.next != self.head):
                last_node = last_node.next
            last_node.next = new_node
            # (3) Point the head to new_node.
            self.head = new_node



    def print_list(self):
        temp = self.head
        while(temp.next != self.head):
            print("{}-->".format(temp.data), end="")
            temp = temp.next
        print("{}-->{}".format(temp.data, temp.next.data))
    


print("Original Circular Linked List:")
cll = CircularLinkedList()
cll.push(5)
cll.push(4)
cll.push(3)
cll.push(2)
cll.push(1)
cll.print_list()
print("\nCircular Linked List After Insertion of 6:")
cll.push(6)
cll.print_list()
