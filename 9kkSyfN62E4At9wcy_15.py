"""


Create a function that takes a list of elements and return the **first** and
**last** elements as a new list.

### Examples

    first_last([5, 10, 15, 20, 25]) ➞ [5, 25]
    
    first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True]
    
    first_last([None, 4, "6", "hello", None]) ➞ [None, None]

### Notes

  * Test input will always contain a minimum of two elements within the list.
  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def first_last(lst):
  array = []
  array.append(lst[0])
  array.append(lst[-1])
  return array

