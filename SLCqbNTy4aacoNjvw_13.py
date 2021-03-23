"""


Create a function that takes a list of items, removes all duplicate items and
returns a new list in the same sequential order as the old list (minus
duplicates).

### Examples

    remove_dups([1, 0, 1, 0]) ➞ [1, 0]
    
    remove_dups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]
    
    remove_dups(["John", "Taylor", "John"]) ➞ ["John", "Taylor"]

### Notes

  * Tests contain lists with both strings and numbers.
  * Tests are case sensitive.
  * Each list item is unique.

"""

def remove_dups(lst):
  seen = []
  for i in range(0, len(lst)):
    if lst[i] not in seen:
      seen.append(lst[i])
  return seen

