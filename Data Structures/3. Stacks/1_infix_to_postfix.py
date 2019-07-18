def infix_to_postfix(expr):
    operator_precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}
    # operator_stack
    stack = []

    # Start the scan from left to right
    for char in expr:
        # If scanned char is not an operand, then output it.
        if char.isalpha():
            print("{}".format(char), end="")

        # Else if the scanned character is an ‘(‘, push it to the stack.
        elif(char == "("):
            stack.append(char)

        # If the scanned character is an ‘)’, pop and output from the stack until an ‘(‘ is encountered.
        elif(char == ")"):
            while(len(stack)>0 and stack[-1] != "("):
                print("{}".format(stack.pop()), end="")
            stack.pop()

        # Pop the operator from the stack until operator_precedence[char] <= operator_precedence[stack[-1]]
        # Push the scanned operator to the stack
        else:
            while(len(stack)>0 and stack[-1]!="(" and operator_precedence[char] <= operator_precedence[stack[-1]]):
                print("{}".format(stack.pop()), end="")

            # If either stack is empty or precedence of scanned opeartor is greater than the top of stack, Push it to stack
            stack.append(char)

    # Pop and output from the stack until it is not empty.
    while(len(stack)>0):
        print("{}".format(stack.pop()), end="")
    print()



print("Example-1: Infix-to-postfix")
infix_to_postfix("a+b*(c-d)")

print("\nExample-2: Infix-to-postfix")
infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i")
