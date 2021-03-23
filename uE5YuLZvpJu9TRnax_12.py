"""


Create a function that takes a mathematical expression in **prefix notation**
as a string and evaluates the expression.

### Examples

    prefix("+ 5 4") ➞  9
    
    prefix("* 12 2") ➞  24
    
    prefix("+ -10 10") ➞  0

### Notes

  * The mathematical expression is valid.
  * Check the **Resources**.
  * Use `//` for division.

"""

def prefix(exp):
    stack = []
    for element in exp.split()[::-1]:
        if not element in '+-*/':
            stack.append(int(element))
        else:
            stack.append(eval("{} {} {}".format(stack.pop(), element, stack.pop())))
    return int(stack.pop())

