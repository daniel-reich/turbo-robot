"""


Create a function that takes a multidimensional list and returns the total
count of numbers in that list.

### Examples

    count_number([["", 17.2, 5, "edabit"]]) ➞ 2
    # 17.2 and 5.
    
    count_number([[[[[2, 14]]], 2, 3, 4]]) ➞ 5
    # 2, 14, 2, 3 and 4.
    
    count_number([["number"]]) ➞ 0

### Notes

Input may be a list of numbers, strings and empty lists.

"""

def count_number(r, c=0):
  if not r: return c
  if type(r[0]) is list:
    r[0] = [x for x in r[0]]
    return count_number(r[0]+r[1:], c)
  if type(r[0]) in [float, int]: c += 1
  return count_number(r[1:], c)

