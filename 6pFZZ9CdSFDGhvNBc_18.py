"""


Create a function that returns `"even"` if a number has an even number of
factors and `"odd"` if a number has an odd number of factors.

### Examples

    factor_group(33) ➞ "even"
    
    factor_group(36) ➞ "odd"
    
    factor_group(7) ➞ "even"

### Notes

  * You don't need to actually calculate the factors to solve this problem.
  * Think about _why_ a number would have an odd number of factors.

"""

import numpy as np
def factor_group(num):
  if np.sqrt(num)*10**len(str(num))%10==0:
    return 'odd'
  else:
    return 'even'

