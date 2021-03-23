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

def automorphic(n):
  squaredNumber = n * n
  strSquaredNumber = str(squaredNumber)
  stringNumber = str(n)
  if strSquaredNumber.endswith(stringNumber):
    return True
  return False

