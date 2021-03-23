"""


You are given a list which may contain sublists. Your task is to find the
depth of the deepest sublist.

  * `[a]` = 1 depth
  * `[[a]]` = 2 depth
  * `[[[a]]]` = 3 depth, etc

### Examples

    deepest([1, [2, 3], 4, [5, 6]]) ➞ 2
    
    deepest([[[[[[[[[[1]]]]]]]]]]) ➞ 10
    
    deepest([1, 4, [1, 4, [1, 4, [1, 4, [5]]]]]) ➞ 5

### Notes

N/A

"""

def deepest(lst):
  mx = 0
  for x in lst:
    if type(x) is list:
      mx=max(mx, deepest(x))
  return mx+1

