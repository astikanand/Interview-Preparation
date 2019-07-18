def check_balanced_bracket(expression):
    stack = []
    balanced = True

    for bracket in expression:
        # If current is opening bracket push to stack
        if (bracket=='(' or bracket=='[' or bracket=='{'):
            stack.append(bracket)

        # If current is not opening bracket, then it must be closing. So stack cannot be empty at this point. 
        elif len(stack)==0:
           balanced = False
           break
        
        # If current is ')' then top of stack can't be '{' or '['.
        elif bracket == ')':
            x = stack.pop()
            if x=='{' or x=='[': 
                balanced = False
                break
        
        # If current is '}' then top of stack can't be '(' or '['.
        elif bracket == '}': 
            x = stack.pop()
            if x=='(' or x=='[':
                balanced = False
                break
        
        # If current is ']' then top of stack can't be '(' or '{'.
        elif bracket == ']': 
            x = stack.pop()
            if x =='(' or x == '{': 
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
