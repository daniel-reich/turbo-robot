"""


Create a function that can nest a flat list to represent an incremental depth
level sequence.

### Examples

    incremental_depth([1, 2]) ➞ [1, [2]]
    
    incremental_depth([1, 2, 3, 4, 5]) ➞ [1, [2, [3, [4, [5]]]]]
    
    incremental_depth([1, 3, 2, 6]) ➞ [1, [3, [2, [6]]]]
    
    incremental_depth(["dog", "cat", "cow"]) ➞ ["dog", ["cat", ["cow"]]]

### Notes

  * The elements do not matter to the function, you should increment by index.
  * Expect the array length to be from 2-20.

"""

def incremental_depth(lst, tr = [], i = -1):
  if i == -1:
    tr = []
    tr.append(lst[i])
    i -= 1
    return incremental_depth(lst,tr,i)
  elif abs(i) == len(lst) + 1:
    return tr
  else:
    l = [lst[i]]
    l.append(tr)
    tr = l
    i -= 1
    return incremental_depth(lst,tr,i)

