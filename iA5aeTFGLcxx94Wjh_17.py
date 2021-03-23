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
  d = {}
  ans = []
  c = 0
  for i in lst:
    if i in d:
      c = ans.count(i)
    if i not in d:
      c = 0
    d[i] = c
    if c < num:
      ans.append(i)
  return ans

