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
  lst=eq.split(' ')
  if lst[-1]=='x':
    if lst[1]=='+':
      x=eval(lst[0])+eval(lst[2])
    else:
      x=eval(lst[0])-eval(lst[2])
  else:
    if lst[0]=='x':
      if lst[1]=='+':
        x=eval(lst[-1])-eval(lst[2])
      else:
        x=eval(lst[-1])+eval(lst[2])
    else:
      if lst[1]=='+':
        x=eval(lst[-1])-eval(lst[0])
      else:
        x=eval(lst[0])-eval(lst[-1])
  return x

