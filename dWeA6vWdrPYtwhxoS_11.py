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

import string
def count_number(lst):
  digits = string.digits
  count = 0
  lst = ((str(lst).replace('[','')).replace(']','')).split(' ')
  for eachvalue in lst:
    for eachletter in eachvalue:
      if eachletter in digits or eachletter == '.':
        count += 1
        break
      else:
        continue
  return count

