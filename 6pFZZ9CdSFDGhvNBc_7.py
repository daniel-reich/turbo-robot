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
  lst = []
  for i in range(1,num+1):
    if num%i == 0:
      lst.append(i)
  if len(lst)%2 == 0:
    return "even"
  else:
    return "odd"

