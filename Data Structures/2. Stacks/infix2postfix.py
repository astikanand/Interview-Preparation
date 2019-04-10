def infixToPostfix(exp):
    prec = { "(":1, "-":2, "+":2, "*":3, "/":3, "%":3, "^":4}
    stack = []
    output = []

    for i in exp:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "0123456789":
            output.append(i)
        elif i == '(':
            stack.append(i) # push to stack
        elif i == ')':
            top = stack.pop()
            while top != '(':
                output.append(top)
                top = stack.pop()
        else:
            # While top of stack has higher or equal precedence output it
            while (len(stack)>0) and (prec[stack[-1]]>= prec[i]): 
                  output.append(stack.pop())
            stack.append(i) # push to stack

    while (len(stack)>0):
        output.append(stack.pop())
    return " ".join(output)

print(infixToPostfix("A*B+C*D"))
print(infixToPostfix("(A+B)*C-(D-E)*(F+G)"))