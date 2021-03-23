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
  if(len(lst)==0):
    return lst
  ans=list()
  for i in range(0,len(lst)):
    check=0
    for j in range(i+1,len(lst)):
      if(lst[i]<=lst[j]):
        check=1
        break
    if(check==0):
      ans.append(lst[i])
  return ans

