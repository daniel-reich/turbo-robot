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
  lst=lst[::-1]
  best, cur=0,0
  curi, s, e=0,0,0
  for i, x in enumerate(lst):
    if cur+x>0:
      cur+=x
    else:
      cur, curi=0, i+1
    if cur>best:
      s,e,best=curi, i+1,cur
  return [best, len(lst)-e, len(lst)-s-1]

