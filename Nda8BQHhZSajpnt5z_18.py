"""


Write a function that returns the greatest common divisor of all list
elements. If the greatest common divisor is `1`, return `1`.

### Examples

    GCD([10, 20, 40]) ➞ 10
    
    GCD([1, 2, 3, 100]) ➞ 1
    
    GCD([1024, 192, 2048, 512]) ➞ 64

### Notes

  * List elements are always greater than `0`.
  * There is a minimum of two list elements given.

"""

def GCD(lst):
  x=[]
  for items in range(1,lst[0]+1):
    if lst[0]%items==0:
      x.append(items)
  
  x.sort()
  x.reverse()
  y=[]
  for items in x:
    c=[]
    for item in lst:
      if item%items==0:
        c.append(True)
      else:
        c.append(False)
    if c.count(False)==0:
      y.append(items)
  
    
  if len(y)==0:
    return 1
  else:
    return max(y)

