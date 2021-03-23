"""


Create a function that validates whether a number `n` is within the bounds of
`lower` and `upper`. Return `False` if `n` is not an **integer**.

### Examples

    int_within_bounds(3, 1, 9) ➞ True
    
    int_within_bounds(6, 1, 6) ➞ False
    
    int_within_bounds(4.5, 3, 8) ➞ False

### Notes

  * The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound, (see example #2). 
  * Bounds will be always given as integers.

"""

def int_within_bounds(n, lower, upper):
  return lower<=n<upper and '.' not in str(n)

