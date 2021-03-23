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

def max_product(n):
  mx = 0
  ans = []
  for i in range(n + 1):
    prod = 1
    temp = [int(x) for x in str(i)]
    for x in temp:
      prod *= x
    if prod > mx:
      mx = prod
      ans = []
    if prod == mx:
      ans.append(i)
  return ans

