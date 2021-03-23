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

def is_num(s):
    return s.lstrip('-').replace('.','',1).isdigit()
    
def prefix(exp):
    exp = exp.replace("/", "//")
    exp = exp.split()
    i = 0
    while len(exp) != 1:
        operands = exp[i + 1:i + 3]
        if exp[i] in ("+", "-", "*", "//") and all(is_num(i) for i in operands):
            operation = exp[i]
            op_1 = exp[i + 1]
            op_2 = exp[i + 2]
            exp[i:i + 3] = [str(eval(op_1 + operation + op_2))]
            i = 0
        else:
            i += 1
    return int(exp[0])

