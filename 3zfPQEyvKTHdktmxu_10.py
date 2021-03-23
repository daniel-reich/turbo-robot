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
  res = []
  for i in range(len(lst)):
    if lst[i] > 0:
      j = i + 1
      while j < len(lst)+1 and sum(lst[i:j]) > 0:
        res.append([sum(lst[i:j]), i, j - 1])
        j += 1
  return sorted(res, key=lambda x : (x[0], x[1]))[-1]

