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
  max_sum = max_start = max_end = curr_sum = 0
  for curr_end, x in enumerate(lst):
    if curr_sum <= 0:
      curr_start, curr_sum = curr_end, x
    else:
      curr_sum += x
    if curr_sum >= max_sum:
      max_sum, max_start, max_end = curr_sum, curr_start, curr_end
  return [max_sum, max_start, max_end]

