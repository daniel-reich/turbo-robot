"""


Write a function that converts a **dictionary** into a **list** of keys-values
**tuples**.

### Examples

    dict_to_list({
      "D": 1,
      "B": 2,
      "C": 3
    }) ➞ [("B", 2), ("C", 3), ("D", 1)]
    
    dict_to_list({
      "likes": 2,
      "dislikes": 3,
      "followers": 10
    }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]

### Notes

Return the elements in the list in alphabetical order.

"""

def dict_to_list(d):
  ke = []
  re = []
  for key in d.keys():
    ke.append(key)
  ke.sort()
  for i in ke:
    re.append((i,d[i]))
  return re

