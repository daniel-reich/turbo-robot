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
  eq = eq.split(" = ")
  if not "x" in eq[0]:
    return eval(eq[0])
  elif eq[0][0] == "x" or "+" in eq[0]:
    eq[0] = eq[0].replace("x",str("-") + eq[1]) 
    return -1 * eval(eq[0])
  else:
    eq[0] = eq[0].replace("x", eq[1])
    return eval(eq[0])

