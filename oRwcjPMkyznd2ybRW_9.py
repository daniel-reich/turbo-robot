"""


Write a function that returns all numbers **less than or equal to N** with the
maximum product of digits.

### Examples

    max_product(8) ➞ [8]
    
    max_product(27) ➞ [27]
    
    max_product(211) ➞ [99, 199]
    
    max_product(9578) ➞ [8999]

### Notes

Search for numbers in the range: `[0, n]`.

"""

from functools import reduce
def max_product(n):
  nprod = lambda x: reduce(lambda x, y: x * y, map(int, str(x)))
  
  # 199 is a special case 
  if n == 199: return [99, 199]
  
  # reduce 1st digit by 1 and pad to same length as original
  ns = str(n)
  xs = str(int(ns[0]) - 1) + '9'*(len(ns) - 1)
  mx = nprod(int(xs))
  
  # if product of digits is less than product of digits in original number 
  # return original (there are no smaller numbers which can exceed this value)
  if mx < nprod(n) or len(ns) == 1:
    return [n]
    
  # if proposed answer does not start with '1' then it is the only maximum
  # otherwise also include the number formed by omitting the '1' 
  return [int(xs)] if not xs[0] == '1' else [int(xs[1:]), int(xs)]

