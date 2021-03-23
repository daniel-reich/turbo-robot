"""


Given a list and a set, return a sorted list with its items in ascending order
but prioritize the elements in the set over the other items in the list.

### Examples

    priority_sort([5, 4, 3, 2, 1], {2, 3}) ➞ [2, 3, 1, 4, 5]
    
    priority_sort([5, 4, 3, 2, 1], {3, 6}) ➞ [3, 1, 2, 4, 5]
    
    priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}) ➞ [-4, -3, -5, -2, -1, 0]

### Notes

  * If the list is empty, return an empty list.
  * If the set is empty there is nothing to prioritize, but the list should still be sorted.
  * The set may contain values that are not in the list.
  * The list may contain duplicates.
  * The list and the set will only contain integer values.

"""

def priority_sort(lst, s):
  return sorted(lst, key=lambda x: (x in s, -x), reverse=True)

