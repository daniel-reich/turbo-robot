"""


Create a function that takes a number `num` and returns its **double
factorial**. Mathematically, the formulas for double factorial are as follows.

If `num` is **even** :

    num !! = num ( num - 2)( num - 4)( num - 6) ... (4)(2)

If `num` is **odd** :

    num !! = num ( num - 2)(num - 4)(num - 6) ... (3)(1)

If num = 0 or num = -1, then num !! = 1 **by convention**.

### Examples

    double_factorial(0) ➞ 1
    
    double_factorial(2) ➞ 2
    
    double_factorial(9) ➞ 945
    # 9*7*5*3*1 = 945
    
    double_factorial(14) ➞ 645120

### Notes

  * Assume all input values are greater than or equal to `-1`.
  * Try to solve it with recursion.
  * Double factorial is not the same as factorial * 2.

"""

def double_factorial(num):
  if num <= 0:
    return 1
  else:
    return num * double_factorial(num-2)

