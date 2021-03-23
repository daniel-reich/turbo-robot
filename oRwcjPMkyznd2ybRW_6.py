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
  def p(k):
    c=1
    for i in str(k):c*=int(i)
    return c
  d={}
  for i in range(n+1):
    if p(i) not in d:d[p(i)]=[i]
    else: d[p(i)].append(i)
  return d[max(d)]

