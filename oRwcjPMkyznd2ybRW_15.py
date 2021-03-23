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

def prod(x):
  r=1
  for i in str(x): r*=int(i)
  return r
​
def max_product(n):
  m,r = 0,[]
  for i in range(n+1):
    x=prod(i)
    if x>m: m,r = x,[i]
    elif x==m: r.append(i)
  return r

