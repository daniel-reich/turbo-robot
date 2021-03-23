"""


Given a _string_ containing an _algebraic equation_ , calculate and **return
the value of x**. You'll only be given equations for simple **addition** and
**subtraction**.

### Examples

    eval_algebra("2 + x = 19") ➞ 17
    
    eval_algebra("4 - x = 1") ➞ 3
    
    eval_algebra("23 + 1 = x") ➞ 24

### Notes

  * There are spaces between every number and symbol in the string.
  * x may be a negative number.

"""

def eval_algebra(eq):
    a, b, c, d, e = eq.split()
    if e=="x":
        return eval(a+b+c)
    elif a=="x":
        return int(e) - int(c) if b=="+" else int(e)+int(c)
    elif c=="x":
        return int(e)-int(a) if b=="+" else int(a)-int(e)

