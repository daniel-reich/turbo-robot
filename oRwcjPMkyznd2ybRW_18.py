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
  out = []
  highest = 0
  for i in range(n+1):
    product = 1
    for j in str(i):
      product *= int(j)
    if product>highest:
      out = [int(i)]
      highest = product
    elif product == highest:
      out.append(int(i))
  return out

