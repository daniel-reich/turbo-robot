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
  max_prod = max(product(i) for i in range(1,n+1))
  return [i for i in range(1,n+1) if product(i)==max_prod]
​
​
​
​
def product(n):
  p = 1
  for i in str(n):
    p*=int(i)
  return p

