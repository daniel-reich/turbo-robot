"""


Create a function that takes a list of numbers and return the number that's
unique.

### Examples

    unique([3, 3, 3, 7, 3, 3]) ➞ 7
    
    unique([0, 0, 0.77, 0, 0]) ➞ 0.77
    
    unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0

### Notes

Test cases will always have exactly one unique number while all others are the
same.

"""

def unique(lst):
  for i in lst:
    n = lst.count(i)
    if n == 1:
      return i

