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
    
    
    def add_2_numbers(self, number):
        # Take 2 pointers to track both the lists, take carry = 0 and also initialize result list.
        temp_1 = self.head
        temp_2 = number.head
        carry = 0
        result = LinkedList()

        # Now while any of temp_1 or temp_2 is there keep going.
        while(temp_1 or temp_2):
            # Get the sum: carry + first_list digit sum if exists else 0 + second_list digit sum if exists else 0.
            digit_sum = carry + (0 if not temp_1 else temp_1.data) + (0 if not temp_2 else temp_2.data)
            # If sum geater than 10 then get the digit and carry separated.
            if(digit_sum >= 10):
                carry = 1
                digit_sum -= 10
            else:
                carry = 0
            
            # Push the digit to result list and update the temp_1 and temp_2 pointers if exists else None.
            result.push(digit_sum)
            temp_1 = None if not temp_1 else temp_1.next
            temp_2 = None if not temp_2 else temp_2.next
        
        # At the end if carry still is not zero, then push carry also to the result list.
        if(carry != 0):
            result.push(carry)
        
        # Lastly, set the head of the list as result list's head.
        self.head = result.head



print("Example-1:")
print("First Number: {}".format(984))
number_1 = LinkedList()
number_1.push(9)
number_1.push(8)
number_1.push(4)
print("Second Number: {}".format(978))
number_2 = LinkedList()
number_2.push(9)
number_2.push(7)
number_2.push(8)
print("Sum of both:")
number_1.add_2_numbers(number_2)
number_1.print_list()

print("\nExample-2:")
print("First Number: {}".format(64957))
number_1 = LinkedList()
number_1.push(6)
number_1.push(4)
number_1.push(9)
number_1.push(5)
number_1.push(7)
print("Second Number: {}".format(48))
number_2 = LinkedList()
number_2.push(4)
number_2.push(8)
print("Sum of both:")
number_1.add_2_numbers(number_2)
number_1.print_list()