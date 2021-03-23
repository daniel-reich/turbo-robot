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

def landscape_type(lst):
  largest = max(lst)
  smallest = min(lst)
  peak = 0
  trough = 0
  left = []
  right = []
  if largest != lst[0] and largest != lst[-1] and lst.count(largest) == 1:
    peak = largest   # must be unique and not on boundaries in order to qualify as a peak
  if smallest != lst[0] and smallest != lst[-1] and lst.count(smallest) == 1:
    trough = smallest   # must be unique and not on boundaries in order to qualify as trough
  if peak == largest:   # confirmed peak, check if it is a mountain
    left = lst[0 : lst.index(peak)]
    right = lst[ lst.index(peak) :]
    if left == sorted(left) and right == sorted(right, reverse=True):
      return 'mountain'
  if trough == smallest:   # confirmed trough, check if it is a valley
    left = lst[0 : lst.index(trough)]
    right = lst[lst.index(trough) :]
    if left == sorted(left, reverse=True) and right == sorted(right):
      return 'valley'
  return 'neither'

