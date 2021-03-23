"""


In this challenge, you have to establish if a given integer `n` is a Sastry
number. If the number resulting from the concatenation of an integer `n` with
its successor is a perfect square, then `n` is a Sastry Number.

Given a positive integer `n`, implement a function that returns `True` if `n`
is a Sastry number, or `False` if it's not.

### Examples

    is_sastry(183) ➞ True
    # Concatenation of n and its successor = 183184
    # 183184 is a perfect square (428 ^ 2)
    
    is_sastry(184) ➞ False
    # Concatenation of n and its successor = 184185
    # 184185 is not a perfect square
    
    is_sastry(106755) ➞ True
    # Concatenation of n and its successor = 106755106756
    # 106755106756 is a perfect square (326734 ^ 2)

### Notes

  * A perfect square is a number with a square root equals to a whole integer.
  * You can expect only valid positive integers greater than 0 as input, without exceptions to handle. Zero is a perfect square, but the concatenation 00 isn't considered as a valid result to check.

"""

def is_sastry(n):
  return int(str(n)+str(n+1))**.5%1==0

