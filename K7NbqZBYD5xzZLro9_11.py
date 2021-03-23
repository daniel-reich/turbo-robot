"""


Create a function that takes a range of numbers and returns the sum of each
digit from `start` to `stop`.

### Examples

    digits_sum(1, 10) ➞ 46
    # total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46
    
    digits_sum(1, 20) ➞ 102
    
    digits_sum(1, 100) ➞ 901

### Notes

`start` and `stop` are inclusive in the range.

"""

from sys import setrecursionlimit
setrecursionlimit(100000000)
def digits_sum(start, stop):
  if start == stop:
      return sum(map(int, str(stop)))
  else:
      return sum(map(int, str(stop))) + digits_sum(start,stop-1)

