"""


Return the coordinates (`[row, col]`) of the element that differs from the
rest.

### Examples

    where_is_waldo([
      ["A", "A", "A"],
      ["A", "A", "A"],
      ["A", "B", "A"]
    ]) ➞ [3, 2]
    
    where_is_waldo([
      ["c", "c", "c", "c"],
      ["c", "c", "c", "d"]
    ]) ➞ [2, 4]
    
    where_is_waldo([
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["P", "O", "O", "O"],
      ["O", "O", "O", "O"]
    ]) ➞ [5, 1]

### Notes

  * The given list will always be a square.
  * Rows and columns are 1-indexed ( **not zero-indexed** ).

"""

import itertools
def where_is_waldo(lst):
  flat_list = list(itertools.chain(*lst))
  unique_list = list(set(list(itertools.chain(*lst))))
  for x in unique_list:
    if flat_list.count(x) == 1:
        unique_element = x
  l2= []
  for idx, val in enumerate(lst):
    l1 = list(set(val))
    if len(l1) > 1:
      l2.append(idx+1)
      l2.append(val.index(unique_element)+1)
  return l2

