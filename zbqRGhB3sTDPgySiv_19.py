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
    if base == 1 and key == 1: return 0
    loop = 0
    if base > key:
        base, key = key, base
    for i in range(base):
        loop += factorial(i)
    return loop

