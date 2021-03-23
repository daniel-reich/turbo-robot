"""


A Kaprekar Number is a positive integer that is equal to a number formed by
first squaring, then splitting and summing its two lexicographical parts:

  * If the quantity of digits of the squared number is even, the left and right parts will have the same length.
  * If the quantity of digits of the squared number is odd, then the right part will be the longer half, with the left part being the shorter or equal to zero if the quantity of digits is equal to 1.

Given a positive integer `n` implement a function that returns `True` if it's
a Kaprekar number, and `False` if it's not.

### Examples

    is_kaprekar(3) ➞ False
    # n² = "9"
    # Left + Right = 0 + 9 = 9 ➞ 9 != 3
    
    is_kaprekar(5) ➞ False
    # n² = "25"
    # Left + Right = 2 + 5 = 7 ➞ 7 != 5
    
    is_kaprekar(297) ➞ True
    # n² = "88209"
    # Left + Right = 88 + 209 = 297 ➞ 297 == 297

### Notes

Trivially, 0 and 1 are Kaprekar Numbers being the only two numbers equal to
their square. Any number formed only by digits equal to _9_ will always be a
Kaprekar Number.

"""

def is_kaprekar(n):
  s = str(n*n)
  s = '0' * (len(s)%2) + s
  return int(s[:len(s)//2]) + int(s[len(s)//2:]) == n

