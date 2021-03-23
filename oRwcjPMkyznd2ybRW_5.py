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

import numpy as np
def max_product(n):
  maximum = max([np.prod([int(y) for y in str(x)]) for x in range(n+1)])
  x = [x for x in range(n+1) if np.prod([int(y) for y in str(x)]) == maximum]
  return x

