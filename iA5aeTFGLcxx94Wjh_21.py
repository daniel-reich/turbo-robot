"""


Create a function that takes two arguments: a list `lst` and a number `num`.
If an element occurs in `lst` more than `num` times, remove the extra
occurrence(s) and return the result.

### Examples

    delete_occurrences([1, 1, 1, 1], 2) ➞ [1, 1]
    
    delete_occurrences([13, True, 13, None], 1) ➞ [13, True, None]
    
    delete_occurrences([True, True, True], 3) ➞ [True, True, True]

### Notes

Do not alter the order of the original list.

"""

def delete_occurrences(lst, num):
  lst.reverse()
  for el in lst:
    if lst.count(el) > num:
      lst.remove(el)
  lst.reverse()
  return lst

