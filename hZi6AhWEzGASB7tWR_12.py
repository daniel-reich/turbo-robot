"""


Write a function that takes a list and determines whether it's strictly
increasing, strictly decreasing, or neither.

### Examples

    check([1, 2, 3]) ➞ "increasing"
    
    check([3, 2, 1]) ➞ "decreasing"
    
    check([1, 2, 1]) ➞ "neither"
    
    check([1, 1, 2]) ➞ "neither"

### Notes

  * The last example does NOT count as strictly increasing, since 1-indexed `1` is not strictly greater than the 0-indexed `1`.
  * Input lists have a minimum length of 2.

"""

def check(lst):
  i=0
  try:
    while i<len(lst)-2:
      if lst[i]>lst[i+1] and lst[i+1]>lst[i+2]:
        i+=1
        continue
      elif lst[i]<lst[i+1] and lst[i+1]<lst[i+2]:
        i+=1
        continue
      else:
        return 'neither'
        break
  except:
    pass
  if lst[1]>lst[0]:
    return 'increasing'
  elif lst[1]<lst[0]:
    return 'decreasing'
  else:
    return 'neither'

