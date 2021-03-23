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
  first = lst[0]
  for el in lst:
    if isinstance(el, str):
      return "Strings not permitted!"
    else:
      if el < first:
        return False
      else:
        first = el
  return True

