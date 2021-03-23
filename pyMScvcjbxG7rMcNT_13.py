"""


Create a function that takes a list and returns the sum of all the items in
that list.

### Examples

    sum_list([1, 2, 3]) ➞ 6
    # 1 + 2 + 3 = 6
    
    sum_list([1, [2, [1]], 3]) ➞ 7
    # 1 + 2 + 1 + 3 = 7

### Notes

  * An item in the list can be another list.
  * Try solving it in a recursive approach without using the built-in `sum()` function.

"""

def sum_list(lst):
  if isinstance(lst[0],int):
    if len(lst)>1:
      return lst[0]+sum_list(lst[1:])
    else:
      return lst[0]
  else:
    if len(lst)>1:
      return sum_list(lst[0])+sum_list(lst[1:])
    else:
      return sum_list(lst[0])

