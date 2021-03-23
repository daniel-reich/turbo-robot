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
  item_count_list = []
  items_set = set(lst)
  for item in items_set:
    item_count_list.append([item, 0])
  delete_indices = []
  for x, i in enumerate(lst):
    item_count_index = [idx for idx, val in enumerate(item_count_list) if val[0] == i][0]
    item_count_list[item_count_index][1] += 1
    if item_count_list[item_count_index][1] > num:
      delete_indices.insert(0, x)
  for index in delete_indices:
    del lst[index]
  return lst

