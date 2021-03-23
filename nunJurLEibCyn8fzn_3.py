"""


Create a function that takes a list of non-negative **integers** and
**strings** and return a new list without the strings.

### Examples

    filter_list([1, 2, "a", "b"]) ➞ [1, 2]
    
    filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
    
    filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]

### Notes

  * Zero is a non-negative integer.
  * The given list only has integers and strings.
  * Numbers in the list should not repeat.
  * The original order must be maintained.

"""

def filter_list(lst):
  all_num = []
  
  for i in lst:
    if type(i) == int:
      all_num.append(i)
    else:
      pass
  return all_num

