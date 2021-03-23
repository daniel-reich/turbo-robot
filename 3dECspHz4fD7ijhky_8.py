"""


Create a function that takes a list of integers and returns the range of
consecutive numbers separated by dash a `-` between `starting` and `ending`
numbers.

  * Separate different ranges by `,` commas.
  * A range of numbers will be considered if **three or more consecutive numbers** are found in the list (see example #1).

### Examples

    numbers_range([-6, -3, -2, -1, 0, 1, 7, 8, 9, 10, 11, 14, 15]) ➞ "-6,-3-1,7-11,14,15"
    # -6 is an alone integer.
    # -3 to 1 is a range of consecutive numbers.
    # 7 to 11 is a range of consecutive numbers.
    # 14 and 15 are consecutive numbers but cannot be considered as a range.
    
    numbers_range([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) ➞ "-3--1,2,10,15,16,18-20"
    
    numbers_range([1, 2, 3, 9, 10, 15, 16, 18, 56, 57]) ➞ "1-3,9,10,15,16,18,56,57"

### Notes

N/A

"""

def numbers_range(ranges):
  if len(ranges) < 2:
    return str(ranges[0]) if ranges else ''
  ranges.append(.1)
  a, b = 0, 0
  parts = []
  while b < len(ranges) - 1:
    if ranges[b] + 1 == ranges[b + 1]:
      b += 1
    else:
      parts.append((a, b))
      b += 1
      a = b
  str_ranges = []
  for a, b in parts:
    if b - a == 0:
      str_ranges.append(str(ranges[a]))
    elif b - a == 1:
      str_ranges.append(str(ranges[a]) + ', ' + str(ranges[b]))
    else:
      str_ranges.append(str(ranges[a]) + '-' + str(ranges[b]))
  return ', '.join(str_ranges)

