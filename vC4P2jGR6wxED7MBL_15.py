"""


Create a function that retrieves every number that is **strictly larger** than
every number that follows it.

### Examples

    larger_than_right([3, 13, 11, 2, 1, 9, 5]) ➞ [13, 11, 9, 5]
    # 13 is larger than all numbers to its right, etc.
    
    larger_than_right([5, 5, 5, 5, 5, 5]) ➞ [5]
    # Must be strictly larger.
    # Always include the last number.
    
    larger_than_right([5, 9, 8, 7]) ➞ [9, 8, 7]

### Notes

The last number in an array is trivially strictly larger than all numbers that
follow it (no numbers follow it).

"""

def larger_than_right(lst):
  y = max(lst)
  g = lst.index(y)
  newlist = lst[g:]
  newerList = []
  for i,v in enumerate(newlist[:-1]):
    if v > max(newlist[i+1:]):
      newerList.append(v)
  
  if len(newlist) > 1:
    if newlist[-2] > newlist[-1]:
      newerList.append(newlist[-1])
  
  if len(newerList) == 0:
    newerList.append(y)
  
  return newerList

