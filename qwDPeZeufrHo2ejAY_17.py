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
    ab, c = eq.split(' = ')
    a, op, b = ab.split()
    if c == 'x':
        return eval(a + op + b)
    if a == 'x':
        if op == '+':
            return eval(c + '-' + b)
        else:
            return eval(c + '+' + b)
    if op == '+':
        return eval(c + '-' + a)
    else:
        return eval(a + '-' + c)

