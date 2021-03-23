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
  new_list = []
  sorted_keys = list(d.keys())
  sorted_keys.sort()
  for k in sorted_keys:
    new_list.append((k,d[k]))
  return new_list

