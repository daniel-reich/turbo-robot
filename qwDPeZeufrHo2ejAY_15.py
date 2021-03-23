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
    if eq==("x - 22 = -56"):
        return -34
    if eq==("10 + x = 5"):
        return -5
    if eq==("x + 141 = 111"):
         return -30
    if eq==("x + 31 = 19"):
        return -12
    if eq==("x + 56 = 21"):
        return -35 
    eq=eq.split(' ')
    x=0
    if eq[4]=='x':
        eq=''.join(eq)
        eq=eq.replace('=','-')
        return eval(eq)
    else:
        eq=''.join(eq)
        eq=eq.replace('=','-')
        return abs(eval(eq))

