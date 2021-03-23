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
  b=eq.split(" ")
  if b[-1]=="x":return eval("".join(b[0:len(b)-2]))
  else:
    if "+" in b:
      b.remove("x")
      b.remove("+")
      return int(b[-1])-int(b[0])
    else:
      if b[0]=="x":return int(b[2])+int(b[-1])
      else:return int(b[0])-int(b[-1])

