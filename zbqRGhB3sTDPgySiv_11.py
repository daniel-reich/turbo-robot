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

import time
from math import factorial
​
facs = {k: factorial(k) for k in range(51)}
​
def mod(base, key):
    loop = 0
    key2 = key
    key = facs[key]
    for i in range(min(base, key2)):
        loop += facs[i] % key
    return loop % key

