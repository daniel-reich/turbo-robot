"""


A number is called **Automorphic number** if its square ends in the same
digits as the number itself. Create a function that takes a number `n` and
returns `True` if it is an Automorphic number, otherwise `False`.

### Examples

    automorphic(1) ➞ True
    
    automorphic(3) ➞ False
    # 3^2 = 9
    
    automorphic(6) ➞ True
    # 6^2 = 36 (ends with 6)

### Notes

N/A

"""

import math
def automorphic(n):
    return str(n) in str(int(math.pow(n, 2)))

