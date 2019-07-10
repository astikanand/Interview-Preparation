#!/bin/python3
import os
import sys



# Complete the evaluate_expression function below.
def max_result_expression(expression, variables):
    """
    Evaluates the prefix expression and calculates the maximum result
    for the given variable ranges.

    Arguments:
      expression (str): the prefix expression to evaluate.
      variables (dict): all the variables in the expression are the keys
          of this dictionary and their values are tuples `(min, max)` that
          define a range (the upper bound `max` is not included).
          
    Returns:
        int or None: the maximum result of the expression for any combination of the accepted
            values. If the expression is invalid, it will return `None`.
    """
    operators = ["+", "-", "*", "/"]
    expr = expression.split()
    expr = expr[::-1]
    stack = []
    result = True
    for i in expr:
        ##
        # Check for operators
        if i in operators:
            if len(stack) >= 2:
                val_1 = stack.pop()
                val_2 = stack.pop()


                # if val_1 is variable
                if not val_1.isdigit() and not val_1.startswith("-"):
                    if(i == "/" or i == "-"):
                        val_1 = str(variables[val_1][0])
                    else:
                        val_1 = str(variables[val_1][1]-1)

                # if val_2 is variable
                if not val_2.isdigit() and not val_2.startswith("-"):
                    val_2 = str(variables[val_2][1]-1)

                if val_1 == "0" and i=="/":
                    result=False
                    break

                val = str(int(eval(val_1 + i + val_2)))
                stack.append(val)
        ##
        # Check if it contains operator and operands both
        elif i.startswith("0") or "+" in i or "-" in i or "*" in i or "/" in i:
            result = False
            break
        # Check for operands
        elif i.isdigit():
            stack.append(i)
        ##
        # Variables
        else:
            stack.append(i)
    
    if(len(stack)==1 and result):
        result = stack.pop()
        # Check if only element left is varaible
        if not result.isdigit() and not result.startswith("-"):
            result = variables[result][1]-1
        result = int(result)
    else:
        result = None

    return result



expression = "* + 2 x y"
variables ={ "x": (0, 2), "y": (2, 4) }
res = max_result_expression(expression, variables)


print(res)