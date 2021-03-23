"""


Write a function that returns the greatest common divisor of all list
elements. If the greatest common divisor is `1`, return `1`.

### Examples

    GCD([10, 20, 40]) ➞ 10
    
    GCD([1, 2, 3, 100]) ➞ 1
    
    GCD([1024, 192, 2048, 512]) ➞ 64

### Notes

  * List elements are always greater than `0`.
  * There is a minimum of two list elements given.

"""

def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def GCD(lst):
  g = gcd(lst[0], lst[1])
  for k in lst[2:]:
    g = gcd(k, g)
  return g

