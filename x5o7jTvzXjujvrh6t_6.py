"""


The iterated square root of a number is the number of times the square root
function must be applied to bring the number **strictly under 2**.

Given an integer, return its iterated square root. Return `"invalid"` if it is
negative.

### Examples

    i_sqrt(1) ➞ 0
    
    i_sqrt(2) ➞ 1
    
    i_sqrt(7) ➞ 2
    
    i_sqrt(27) ➞ 3
    
    i_sqrt(256) ➞ 4
    
    i_sqrt(-1) ➞ "invalid"

### Notes

Idea for iterated square root by Richard Spence.

"""

from math import sqrt
def i_sqrt(n):
  if n > 0:
    count = 0
    while n >= 2:
      count += 1
      n = sqrt(n)
    return count
  return 'invalid'

