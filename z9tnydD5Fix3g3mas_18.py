"""


Create a function that checks if the sub-lists in a list adhere to the
specified pattern.

### Examples

    check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
    
    check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True
    
    check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True

### Notes

  * The length of the pattern will always be the same as the length of the (main) list.
  * The pattern does not necessarily have to be alphabetically ordered (see last example).

"""

def check_pattern(lst, pattern):
  d={}
  z=""
  m=[]
  for l in range(len(lst)):
    for e in lst[l]:
      z=z+str(e)
    if l==len(lst)-1:
      if z in d.keys():
        if d[z] != pattern[l]:
          return False
        else:
          break
      else:
        if pattern[l] in m and z not in d.keys():
          return False
        d[z]=pattern[l]
        m.append(pattern[l])
        break
    else:
      if z in d.keys():
        if d[z] != pattern[l]:
          return False
        else:
          z=""
          continue
      else:
        if pattern[l] in m and z not in d.keys():
          return False
        d[z]=pattern[l]
        z=""
        m.append(pattern[l])
  return True

