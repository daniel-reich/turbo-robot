"""


Create a function that takes a list of lists and return the length of the
missing list.

### Examples

    find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3
    
    find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3
    
    find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2

### Notes

  * Test input lists won't always be sorted in order of length.
  * If the list of lists is `None` or empty, your function should return `False`.
  * If a list within the parent list is `None` or empty, return `False`.
  * There will always be a missing element and its length will be between the given lists.

"""

def find_missing(lst):
  lengths = []
  if lst == []:
    return False
  elif lst == None:
    return False
    
  for small_list in lst:
    if small_list == []:
      return False
    length= len(small_list)
    lengths.append(length)
    
  mini = min(lengths)
  maxi = max(lengths)
  compare = set(range(mini,maxi+1))
  lengths_set = set(lengths)
  difference = compare - lengths_set
  diff = list(difference)
  return diff[0]

