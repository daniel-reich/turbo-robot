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

def max_product(n,c=0):
  max=0;l=[]
  for i in range(1,n+1):
    p=1
    for j in str(i):
      p=p*int(j)
    if max<p:
      max=p
      a=i
      if c==1:
        l=[]
        c=0
    elif max==p:
      l.append(i)
      c=1
  l=[a]+l
  return l

