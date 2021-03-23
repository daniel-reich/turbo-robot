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
  odd_cnt = 0
  even_cnt = 0
  
  for num in lst:
    if num % 2 != 0:
      odd_cnt += 1
    else:
      even_cnt += 1
      
  if odd_cnt > even_cnt:
    return True
  else:
    return False

