"""


 **Dividing by 0** is a huge mistake and should be avoided at all costs.

Create a function that when given a _math expression_ as a _string_ , return
`True` if at any point, the expression involves **dividing by 0**.

### Examples

    catch_zero_division("2 / 0") ➞ True
    
    catch_zero_division("4 / (2 + 3 - 5)") ➞ True
    
    catch_zero_division("2 * 5 - 10") ➞ False

### Notes

Multiplication signs will be given as an asterisk `*`.

"""

def catch_zero_division(expr):
  try:
    eval(expr)
  except ZeroDivisionError:
    return True
  return False

