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
  # numbers that are perfect squares have an odd number of factors
  # others have an even number of factors
  i = 1
  while i*i <= num:
    if i*i == num:
      return 'odd'
    i += 1
  return 'even'

