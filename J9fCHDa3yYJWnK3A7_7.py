"""


A **happy number** is a number which yields a `1` by repeatedly summing up the
square of its digit. If such a process results in an endless cycle of numbers
containing `4`, the number is said to be an **unhappy number**.

Create a function that accepts a number and determines whether the number is a
_happy number_ or not. Return `True` if so, `False` otherwise.

### Examples

    is_happy(67) ➞ False
    
    is_happy(89) ➞ False
    
    is_happy(139) ➞ True
    
    is_happy(1327) ➞ False
    
    is_happy(2871) ➞ False
    
    is_happy(3970) ➞ True

### Notes

  * You are expected to solve this challenge via recursion.
  * You can check on the **Resources** tab for more details about recursion.
  * A non-recursive version of this challenge can be found in [here](https://edabit.com/challenge/rGAcibgZ6u9MtasfW).

"""

def is_happy(n):
  if n == 1:
    return True
  elif n == 4:
    return False
  else:
    digits = [int(e) for e in str(n)]
    n = 0
    for digit in digits:
      n += digit ** 2
    return is_happy(n)

