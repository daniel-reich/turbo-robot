"""
Create a function that checks if a given integer is exactly the factorial of
an integer or not. `True` if it is, `False` otherwise.

### Examples

    is_factorial(2) ➞ True
    # 2 = 2 * 1 = 2!
    
    is_factorial(27) ➞ False
    
    is_factorial(24) ➞ True
    # 24 = 4 * 3 * 2 * 1 = 4!

### Notes

  * No error handling is necessary. Inputs are all positive integers.
  * Alternatively, you can solve this with a recursive approach.
  * There are similar versions of this challenge that is a bit more challenging than this one (a [recursive](https://edabit.com/challenge/zhqL89ZWgbxbixsdD) and a [non-recursive](https://edabit.com/challenge/f24TDCGbYRjGfALQp)).

"""

def fact(n):
    return n < 2 or n * fact(n - 1)
​
​
def is_factorial(n):
  verdict = False
  x = 1
  fact_x = x
  while fact_x <= n:
    if fact_x == n:
      verdict = True
      break
    x += 1
    fact_x = fact(x)
  return verdict

