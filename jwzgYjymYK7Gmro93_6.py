"""


Create a function that returns the indices of all occurrences of an item in
the list.

### Examples

    get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]
    
    get_indices([1, 5, 5, 2, 7], 7) ➞ [4]
    
    get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]
    
    get_indices([1, 5, 5, 2, 7], 8) ➞ []

### Notes

  * If an element does not exist in a list, return `[]`.
  * Lists are zero-indexed.
  * Values in the list will be value-types (don't need to worry about nested lists).

"""

def get_indices(lst, el):
    return [i  for i in range(0, len(lst), 1) if el == lst[i]]

