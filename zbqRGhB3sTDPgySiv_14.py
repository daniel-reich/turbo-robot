"""


Modify the inefficient code in the **Code** tab so it can pass the tests.

### Examples

    mod(1, 1) ➞ 0
    
    mod(5, 5) ➞ 34
    
    mod(13, 27 ) ➞ 522956314
    
    mod(8000, 30) ➞ 9157958657951075573395300940314

### Notes

  * The variables will be natural numbers.
  * If necessary, there is a hint in the **Tests** tab.

"""

from math import factorial
​
def mod(base, key):
  if base > key:
    base = key
  loop = 1
  key = factorial(key)
  f = 1
  for i in range(1, base):
    f = f * i
    loop += f % key
  return loop % key

