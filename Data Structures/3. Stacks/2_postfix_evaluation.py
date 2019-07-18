def evaluate_postfix(expression):
    expr = expression.split()
    stack = []
    for i in expr:
        if i.isdigit():
            stack.append(i)
        else:
            val1 = stack.pop() 
            val2 = stack.pop()
            stack.append(str(eval(val2 + i + val1)))

    print(stack.pop())


print("Example-1: evaluate_postfix('12 3 *')")
evaluate_postfix('12 3 *')

print("Example-2: evaluate_postfix('2 3 10 * + 9 -')")
evaluate_postfix('2 3 10 * + 9 -')
