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
  def denominators(nums):
    tr = []
    for num in nums:
      factors = []
      for n in range(1, num + 1):
        if num%n==0:
          factors.append(n)
      tr.append(factors)
    return tr
  def common(lsts):
    c = set()
    
    for lst in lsts:
      for i in lst:
        valid = True
        for l in lsts:
          if i not in l:
            valid = False
            break
        if valid == True:
          c.add(i)
    
    return c
  
  dens = denominators(lst)
  comm = common(dens)
  
  return max(comm)

