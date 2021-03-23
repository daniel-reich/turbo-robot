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
  counteven=0
  countodd=0
  for a in range(0,len(lst)):
    if lst[a]%2!=0:
      counteven+=1
    else:
      countodd+=1
  if counteven>countodd:
    return True
  else:
    return False

