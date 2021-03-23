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

OP = {'+':int.__add__, '-':int.__sub__, '*':int.__mul__, '/':int.__floordiv__}
def prefix(exp):
    def calc():
        i = items.pop(0)
        return OP[i](calc(), calc()) if i in OP else int(i)
    items = exp.split()
    return calc()

