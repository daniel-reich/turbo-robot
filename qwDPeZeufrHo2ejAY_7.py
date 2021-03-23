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
  list1 = eq.split()
  result = []
  
  for item in list1:
    try:
      result.append(int(item))
    except:
      result.append(item)
      
  if result[4] == 'x':
    if result[1] == '+':
      return result[0] + result[2]
    return result[0] - result[2]
  elif result[0] == 'x':
    if result[1] == '+':
      return result[4] - result[2]
    return result[4] + result[2]
  elif result[1] == '+':
    return result[4] - result[0]
  return (result[4] - result[0]) * -1

