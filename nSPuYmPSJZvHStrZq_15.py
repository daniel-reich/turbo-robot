"""


Given a list, return `True` if there are more odd numbers than even numbers,
otherwise return `False`.

### Examples

    oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ True
    
    oddeven([1]) ➞ True
    
    oddeven([13452394823795273847528572346]) ➞ False

### Notes

All lists will have at least 1 item.

"""

def oddeven(lst):
  def checkOdd(a):
    if a % 2 == 1:
      return True
    return False
    
  oddNum = list(filter(checkOdd, lst))
  if len(oddNum) > len(lst) // 2:
    return True
  return False

