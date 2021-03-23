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

def sqr_sum_digits(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n //= 10
    return s
​
def is_happy(n):
    if n == 4 or n == 1:
        return n == 1
    return is_happy(sqr_sum_digits(n))
