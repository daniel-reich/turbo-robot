"""


Create a function that returns the sum of missing numbers.

### Examples

    sum_missing_numbers([1, 3, 5, 7, 10]) ➞ 29
    # 2 + 4 + 6 + 8 + 9
    
    sum_missing_numbers([10, 7, 5, 3, 1]) ➞ 29
    
    sum_missing_numbers([10, 20, 30, 40, 50, 60]) ➞ 1575

### Notes

The minimum and maximum value of the given list are the inclusive bounds of
the numeric range to consider when searching for missing numbers.

"""

def sum_missing_numbers(lst):
  lst = sorted(lst)
  min_range = lst[0]
  max_range = lst[-1]
  total = 0
  if min_range > max_range:
    for eachnumber in range(max_range,min_range+1):
      if eachnumber not in lst:
        total += eachnumber
    print(total)
  else:
    for eachnumber in range(min_range,max_range+1):
      if eachnumber not in lst:
        total += eachnumber
    return total

