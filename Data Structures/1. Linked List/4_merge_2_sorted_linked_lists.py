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
    

    def merge_2_sorted_linked_lists(self, sorted_list_2):
        # Take 2 pointers temp_1 and temp_2 to track both lists and a stack to put the data.
        temp_1 = self.head
        temp_2 = sorted_list_2.head
        stack = []

        # While both temp_1 and temp_2 are exists keep on going:
        while(temp_1 and temp_2):
            # If data of temp_1 is lesser temp_1 is selected and incremented else temp_2 is selected and incrmented.
            if(temp_1.data <= temp_2.data):
                stack.append(temp_1.data)
                temp_1 = temp_1.next
            else:
                stack.append(temp_2.data)
                temp_2 = temp_2.next
        
        # If elements are left in temp_1, push all of them to stack.
        while(temp_1):
            stack.append(temp_1.data)
            temp_1 = temp_1.next
        
        # If elements are left in temp_2, push all of them to stack.
        while(temp_2):
            stack.append(temp_2.data)
            temp_2 = temp_2.next
        
        # Now, finally make head point to None and create the linked_list from popping from stack and pushing all nodes to it.
        self.head = None
        while(stack):
            self.push(stack.pop())



print("First Sorted Linked List:")
linked_list_1 = LinkedList()
linked_list_1.push(5)
linked_list_1.push(4)
linked_list_1.push(1)
linked_list_1.print_list()
print("\nSecond Sorted Linked List:")
linked_list_2 = LinkedList()
linked_list_2.push(9)
linked_list_2.push(8)
linked_list_2.push(6)
linked_list_2.push(3)
linked_list_2.push(2)
linked_list_2.print_list()
print("\nMerged List:")
linked_list_1.merge_2_sorted_linked_lists(linked_list_2)
linked_list_1.print_list()