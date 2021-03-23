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
  cur_count = 0
  max_count = 0
  
  for char in str(lst):
    if char == "[":
      cur_count += 1
      if cur_count > max_count:
        max_count = cur_count
    elif char == "]":
      cur_count -= 1
  
  return max_count

