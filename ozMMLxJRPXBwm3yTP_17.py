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

def is_factorial(n):
    from math import factorial
    x=[i*factorial(i-1) for i in range(1,7)]
    if n in x:
        return True
    else:
        return False

