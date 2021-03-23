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
  depth = 1
  newlst = lst
  while True:
    lst = newlst
    newlst = []
    lst = list(filter(lambda x: isinstance(x,list),lst))
    if not lst:
      return depth
    else:
      depth += 1
      for el in lst:
        newlst.extend(el)

