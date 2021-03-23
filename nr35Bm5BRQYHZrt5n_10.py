"""


Create a function that determines if there is an upward trend.

### Examples

    upward_trend([1, 2, 3, 4]) ➞ True
    
    upward_trend([1, 2, 6, 5, 7, 8]) ➞ False
    
    upward_trend([1, 2, 3, "4"]) ➞ "Strings not permitted!"
    
    upward_trend([1, 2, 3, 6, 7]) ➞ True

### Notes

  * If there is a string element in the list, return `"Strings not permitted!"`.
  * The numbers don't have to be consecutive (e.g. `[1, 3, 5]` should still return `True`).

"""

def upward_trend(lst):
  true = 0
  t = 0
  re = True
  for a in lst:
    if isinstance(a,str):
      re = False
      t = 1
  if re:
    for a in range(len(lst)-1):
      if lst[a] < lst[a+1]:
        true = true + 1
      else:
        true = 0
  if true == len(lst) - 1 and re:
    return True
  elif t == 1:
    return "Strings not permitted!"
  else:
    return False

