"""


Create a function that determines whether elements in an array can be re-
arranged to form a consecutive list of numbers where **each number appears
exactly once**.

### Examples

    cons([5, 1, 4, 3, 2]) ➞ True
    // Can be re-arranged to form [1, 2, 3, 4, 5]
    
    cons([5, 1, 4, 3, 2, 8]) ➞ False
    
    cons([5, 6, 7, 8, 9, 9]) ➞ False
    // 9 appears twice

### Notes

N/A

"""

def cons(lst):
  if len(set(lst)) != len(lst):
    return False
  else:
    lst.sort()
    i = 0
    for num in lst:
      if i == 0:
        i += 1
        continue
      else:
        if num - lst[i - 1] != 1:
          return False
        i += 1
  return True

