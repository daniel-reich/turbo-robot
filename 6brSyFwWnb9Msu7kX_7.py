"""


Write a function that sorts the **positive numbers** in **ascending order** ,
and keeps the **negative numbers** untouched.

### Examples

    pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]
    
    pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]
    
    pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]
    
    pos_neg_sort([]) ➞ []

### Notes

  * If given an empty list, you should return an empty list.
  * Integers will always be either positive or negative (0 isn't included in the tests).

"""

def pos_neg_sort(lst):
  sorted_lst = sorted(filter(lambda n: n >= 0, lst))
  s_i = 0
  res = []
  for i in range(len(lst)):
    if lst[i] < 0:
      res.append(lst[i])
    else:
      res.append(sorted_lst[s_i])
      s_i += 1
  return res

