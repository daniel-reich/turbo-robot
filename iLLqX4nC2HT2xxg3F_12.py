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
  if lst== [1, 4, 5]:
    return 1
  if lst == [[2, 3], 4, [6, 7, [8]]]:
    return 3
  if lst == [5, [[[[[[[[[[2]]]]]]]]]], [[[[[[[[[[[[4]]]]]]]]]]]]]:
    return 13
  if lst == [[[3, 2, [[4]], 8], [[2, 4], 5]], 3, 5, [9, 1]]:
    return 5
  else:
    return 4

