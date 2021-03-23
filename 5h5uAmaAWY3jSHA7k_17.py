"""


A **mountain** is a list with **exactly one peak**.

  * All numbers to the left of the **peak** are increasing.
  * All numbers to the right of the **peak** are decreasing.
  * The peak CANNOT be on the boundary.

A **valley** is a list with **exactly one trough**.

  * All numbers to the left of the **trough** are decreasing.
  * All numbers to the right of the **trough** are increasing.
  * The trough CANNOT be on the boundary.

Some examples of **mountains** and **valleys** :

    Mountain A:  [1, 3, 5, 4, 3, 2]   # 5 is the peak
    Mountain B:  [-1, 0, -1]   # 0 is the peak
    Mountain B:  [-1, -1, 0, -1, -1]   # 0 is the peak (plateau on both sides is okay)
    
    Valley A: [10, 9, 8, 7, 2, 3, 4, 5]   # 2 is the trough
    Valley B: [350, 100, 200, 400, 700]  # 100 is the trough

Neither **mountains** nor **valleys** :

    Landscape A: [1, 2, 3, 2, 4, 1]  # 2 peaks (3, 4), not 1
    Landscape B: [5, 4, 3, 2, 1]  # Peak cannot be a boundary element
    Landscape B: [0, -1, -1, 0, -1, -1]  # 2 peaks (0)

Based on the rules above, write a function that takes in a list and returns
either `"mountain"`, `"valley"`, or `"neither"`.

### Examples

    landscape_type([3, 4, 5, 4, 3]) ➞ "mountain"
    
    landscape_type([9, 7, 3, 1, 2, 4]) ➞ "valley"
    
    landscape_type([9, 8, 9]) ➞ "valley"
    
    landscape_type([9, 8, 9, 8]) ➞ "neither"

### Notes

  * A **peak** is not exactly the same as the **max** of a list. The **max** is a unique number, but a list may have multiple peaks. However, if there exists only one peak in a list, then it is true that the peak = max.
  * See comments for a hint.

"""

def mountain(lst,x):
  state = 'up'
  while x+1<len(lst):
    if state == 'up':
      if lst[x] > lst[x+1]:
        state = 'down'
    elif state == 'down':
      if lst[x] < lst[x+1]:
        return 'neither'
    x += 1
  if state == 'down':
    return 'mountain'
  return 'neither'
​
def valley(lst,x):
  state = 'down'
  while x+1<len(lst):
    if state == 'down':
      if lst[x] < lst[x+1]:
        state = 'up'
    elif state == 'up':
      if lst[x] > lst[x+1]:
        return 'neither'
    x += 1
  if state == 'up':
    return 'valley'
  return 'neither'
​
def landscape_type(lst):
  x = 1
  landscape = "neither"
  while x<len(lst):
    if lst[x] > lst[x-1]:
      landscape = mountain(lst,x)
      break
    elif lst[x] < lst[x-1]:
      landscape = valley(lst,x)
      break
    x+=1
  return landscape

