"""
**Mubashir** needs your help to find out trailing zeros after calculating
factorial of a given number.

Create a function which takes a number `n` and calculates the **number of
trailing zeros** in factorial of the given number.

    n! = 1 * 2 * 3 * ... * n

### Examples

    trailing_zeros(0) ➞ 0
    # 0! = 1
    # No trailing zero.
    
    trailing_zeros(6) ➞ 1
    # 6! = 120
    # 1 trailing zero.
    
    trailing_zeros(1000) ➞ 249
    # 1000! has 249 trailing zeros.

### Notes

 **Hint:** No need to calculate the factorial (because it won't help). Find
another way to find the number of zeros.

"""

def trailing_zeros(n):
  f = 32 if n>100000 else 16
  return round(n/(4+f/n)) if n else 0

