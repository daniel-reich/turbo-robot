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

def factor_group(num):
  count = 0
  for ix in range(num):
    if num % (ix + 1) == 0:
      count += 1
  if count % 2 == 0:
    return 'even'
  else:
    return 'odd'

