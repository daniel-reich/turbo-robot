"""


Create a function that takes a list of **numbers or strings** and returns a
list with the items from the original list stored into sublists. Items of the
same value should be in the same sublist.

### Examples

    advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
    
    advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
    
    advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

### Notes

The sublists should be returned in the order of each element's first
appearance in the given list.

"""

def find(lst, item):
  try:
    x = lst.index(item)
  except ValueError:
    return -1
  else:
    return x
def advanced_sort(lst):
  unique_chars = []
  for item in lst:
    if find(unique_chars, item) == -1:
      unique_chars.append(item)
  sorted_lst = [[] for i in unique_chars]
  for item in lst:
    sorted_lst[find(unique_chars, item)].append(item)
  return sorted_lst

