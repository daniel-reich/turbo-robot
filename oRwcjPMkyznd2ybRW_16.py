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
  def prod_of_digits(n):
    prod = 1
    
    s = str(n)
    
    for digit in s:
      prod *= int(digit)
    
    return prod
  
  maxprod = 0
  maxdigits = []
  
  for num in range(1, n+1):
    prod = prod_of_digits(num)
    if prod > maxprod:
      maxdigits = [num]
      maxprod = prod
    elif prod == maxprod:
      maxdigits.append(num)
  
  return maxdigits

