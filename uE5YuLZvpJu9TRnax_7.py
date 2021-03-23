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

def calculator(a, operator, b):
    return {"+": a + b, "-": a - b, "*": a * b, "/": a // b}[operator]
​
​
def prefix(exp):
    expression = exp.split()[::-1]
    stack = []
    for e in expression:
        if "-" in e:
            if e[1:].isdigit():
                stack.append(int(e))
            else:
                stack.append(calculator(stack.pop(), e, stack.pop()))
        elif e.isdigit():
            stack.append(int(e))
        else:
            stack.append(calculator(stack.pop(), e, stack.pop()))
    return stack[0]

