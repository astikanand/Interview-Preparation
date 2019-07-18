def evaluatePostfix(exp):
    stack = []
    for i in exp:
        # If the scanned character is an operand/number push it to the stack
        if i.isdigit():
            stack.append(i) # push 

        # If the scanned character is an operator, pop two elements from stack and apply it.
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(str(eval(val2 + i + val1)))

    return int(stack.pop())


print(evaluatePostfix("231*+9-"))
 