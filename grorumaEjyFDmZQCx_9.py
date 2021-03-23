"""


A wristband can have 4 patterns:

  1. **horizontal** : each item in a row is identical.
  2.  **vertical** : each item in each column is identical.
  3.  **diagonal left** : each item is identical to the one on it's upper left or bottom right.
  4.  **diagonal right** : each item is identical to the one on it's upper right or bottom left.

You are shown an **incomplete section** of a wristband.

Write a function that returns `True` if the section can be correctly
classified into one of the 4 types, and `False` otherwise.

### Examples

    is_wristband([
      ["A", "A"],
      ["B", "B"],
      ["C", "C"]
    ]) ➞ True 
    # Part of horizontal wristband.
    
    is_wristband([
      ["A", "B"],
      ["A", "B"],
      ["A", "B"]
    ]) ➞ True 
    # Part of vertical wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["C", "A", "B"],
      ["B", "C", "A"],
      ["A", "B", "C"]
    ]) ➞ True
    # Part of diagonal left wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["B", "C", "A"],
      ["C", "A", "B"],
      ["A", "B", "A"]
    ]) ➞ True
    # Part of diagonal right wristband.

### Notes

N/A

"""

import copy
def is_wristband(lst):
  # horizontal pattern
  for i in range(len(lst)):
    if lst[i].count(lst[i][0]) != len(lst[i]):
      break
  else:
    return True
    
  # vertical pattern
  tmp = copy.deepcopy(lst)
  tmp = ([list(i) for i in zip(*tmp)])
  for i in range(len(tmp)):
    if tmp[i].count(tmp[i][0]) != len(tmp[i]):
      break
  else:
    return True
    
  # diagonal \\ pattern
  n = 0
  tmp = copy.deepcopy(lst)
  tmp[0][len(tmp[0]) - 1] = tmp[len(tmp) - 1] [0] = None
  for i in range(len(tmp)):
    tmp[i] = tmp[i][n:] + tmp[i][:n]
    n += 1
    if n == len(tmp):
      n = 0
  tmp = ([list(i) for i in zip(*tmp)])
  for i in range(len(tmp)):
    tmp[i] = list(filter(None, tmp[i]))
  for i in range(len(tmp)):
    if len(tmp[i]) == 4 and tmp[i][0] == tmp[i][1] and tmp[i][2] == tmp[i][3]:
      continue
    elif tmp[i].count(tmp[i][0]) != len(tmp[i]):
      break
  else:
    return True
    
  # diagonal // pattern
  n = 0
  tmp = copy.deepcopy(lst)
  tmp[0][0] = tmp[len(tmp) - 1] [len(tmp[0]) - 1] = None
  for i in range(len(tmp)):
    tmp[i] = tmp[i][-n:] + tmp[i][:-n]
    n += 1
    if n == len(tmp):
      n = 0
  tmp = ([list(i) for i in zip(*tmp)])
  for i in range(len(tmp)):
    tmp[i] = list(filter(None, tmp[i]))
  for i in range(len(tmp)):
    if len(tmp[i]) == 4 and tmp[i][0] == tmp[i][1] and tmp[i][2] == tmp[i][3]:
      continue
    elif tmp[i].count(tmp[i][0]) != len(tmp[i]):
      break
  else:
    return True
    
  return False

