"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(num):
  from itertools import permutations as p
  def get_nums(n):
    l = list(str(n))
    nl = []
    for item in l:
      nl.append(int(item))
    l = nl
    del nl
​
    perms = list(p(l))
​
    nums = set()
​
    for perm in perms:
      l = list(perm)
​
      ns = ''
      for item in l:
        ns += str(item)
      
      n = int(ns)
​
      nums.add(n)
    
    return sorted(nums)
  
  gn = get_nums(num)
​
  numindex = None
  for n in range(0, len(gn)):
    tnum = gn[n]
    if tnum == num:
      numindex = n
      break
  
  try:
    next_highest = gn[numindex + 1]
  except IndexError:
    next_highest = num
  
  return next_highest

