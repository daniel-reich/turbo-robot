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
​
def max_product(n):
  highest = 1
  ret = []
  for i in range(n+1):
    prod = reduce((lambda x, y: x * y), [int(digit) for digit in str(i)])
    if prod > highest:
      highest = prod
      ret = [i]
    elif prod == highest:
      ret.append(i)
    
  return ret

