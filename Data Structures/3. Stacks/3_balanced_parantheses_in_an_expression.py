def check_balanced_bracket(expression):
    stack = []
    balanced = True

    for bracket in expression:
        # If current is opening bracket push closing bracket to stack
        if bracket=='(':
            stack.append(')')
        elif bracket=='{':
            stack.append('}')
        elif bracket=='[':
            stack.append(']')
        
        # If current is not opening bracket or the bracket doesnt match the top of stack -> Unbalanced
        elif not stack or stack.pop() != bracket:
           balanced = False
           break
    
    # If Stack is empty it is balanced else not balanced
    if stack or not balanced:
        print("Not Balanced")
    else:
        print("Balanced")


print("Example-1: check_balanced_bracket('[()]{}{[()()]()}')")
check_balanced_bracket('[()]{}{[()()]()}')
print("\nExample-2: check_balanced_bracket('[(])')")
check_balanced_bracket('[(])')
