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
 great=0
 lst=[0]
 for i in range(0,n+1):
  result=1
  for b in str(i):
   result=result*int(b)
  if result==great:
   lst.append(i)
  if result>great:
   lst.clear()
   lst.append(i)
   great=result
​
 return lst

