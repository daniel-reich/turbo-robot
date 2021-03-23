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

def count_number(lst):
  sum_ = 0
  for i in range(len(lst)):
    if type(lst[i]) == list:
      sum_ += count_number(lst[i])
    elif type(lst[i]) == int or type(lst[i]) == float:
      sum_ += 1
  return sum_
