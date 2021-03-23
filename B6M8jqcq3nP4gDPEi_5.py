"""


Write a function that extracts the max value of a number in a list. If there
are **two or more** max values, return it **as a list** , otherwise, return
the **number**. This process could be relatively easy with some of the built-
in list functions but the required approach is **recursive**.

### Examples

    iso_group([31, 7, 2, 13, 7, 9, 10, 13]) ➞ 31
    
    iso_group([1, 3, 9, 5, 1, 7, 9, -9]) ➞ [9, 9]
    
    iso_group([97, 19, -18, 97, 36, 23, -97]) ➞ [97, 97]
    
    iso_group([-31, -7, -13, -7, -9, -13]) ➞ [-7, -7]
    
    iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) ➞ [-1, -1]
    
    iso_group([107, 19, -18, 79, 36, 23, 97]) ➞ 107

### Notes

You can read more about recursion (see the **Resources** tab) if you aren't
familiar with it yet or haven't fully understood the concept before taking up
this challenge.

"""

def iso_group(lst, first=True):
  """The ugliest function due to ugly challenge"""
  if len(lst) < 2: return lst
  res = iso_group(lst[1:], False)
  if res[0] == lst[0]:
    res.append(lst[0])
  elif res[0] < lst[0]:
    res = [lst[0]]
  return res[0] if first and len(res)==1 else res

