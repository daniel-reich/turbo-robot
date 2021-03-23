"""


For a given list, determine the biggest possible sum between consecutive
terms, as well as the initial and final position of the terms.

### Examples

    big_sub([4, -3, 5, -7, 5]) ➞ [6 (sum), 0 (start), 2 (end)]
    
    big_sub([4, -3, -5, 7, 5]) ➞ [12, 3, 4]
    
    big_sub([2, -3, 2, -3, 2]) ➞ [2, 4, 4]

### Notes

  * If the biggest sum is repeated at several intervals, return the starting and ending positions of the latest interval.
  * The list will always have positive numbers.

"""

def big_sub(lst):
  res = [0, 0, 0]
  sum = 0
  for cpos, val in enumerate(lst):
    if sum <= 0:
      spos =  cpos
      sum = val
    else:
      sum += val
    if sum >= res[0]:
      res[0], res[1], res[2] = sum, spos, cpos
  return res

