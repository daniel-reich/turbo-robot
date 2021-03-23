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
  lhs_rhs = eq.split("=")
  if "x" in lhs_rhs[1]:
    return eval(lhs_rhs[0])
  elelents = lhs_rhs[0][:-1].split(" ")
  if "x" in elelents[0]:
    return eval(lhs_rhs[1] + elelents[1] + "-" + elelents[2])
  return eval(elelents[1] + "(" + lhs_rhs[1] + "-" + elelents[0] + ")")

