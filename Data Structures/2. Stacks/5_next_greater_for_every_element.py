def next_greater_for_every_element(arr):
    n = len(arr)
    stack = []
  
    # Push the first element to stack 
    stack.append(arr[0])

    print("Element -- NGE")
  
    # Iterate for rest of the elements 
    for i in range(1, n): 
        current = arr[i] 

        # If stack is not empty, then pop an element from stack as popped_element
        if stack:  
            popped_element = stack.pop() 
  
            # If popped_element is smaller than current, then current is NGE for popped element
            # keep popping while popped elements are smaller than current and stack is not empty
            while popped_element < current: 
                print("{} -------> {}".format(popped_element, current))
                if not stack:
                    break
                popped_element = stack.pop()
  
            # If popped_element is greater than next, then push the popped_element back to stack
            if popped_element > current:
                stack.append(popped_element) 
  
        # Push current to stack so that we can find next greater for it.
        stack.append(current)
    
    # After iterating over the loop, the remaining elements in stack do not have the next greater 
    # so -1 for them
    while stack: 
        popped_element = stack.pop()
        current = -1
        print("{} -------> {}".format(popped_element, current))



print("Example-1: next_greater_for_every_element([4, 5, 2, 25])")
next_greater_for_every_element([4, 5, 2, 25])
print("\nExample-2: next_greater_for_every_element([13, 7, 6, 12])")
next_greater_for_every_element([13, 7, 6, 12])
print("\nExample-3: next_greater_for_every_element([11, 13, 21, 3])")
next_greater_for_every_element([11, 13, 21, 3])
