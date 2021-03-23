"""


Write a function to reverse a list.

### Examples

    reverse([1, 2, 3, 4]) ➞ [4, 3, 2, 1]
    
    reverse([9, 9, 2, 3, 4]) ➞ [4, 3, 2, 9, 9]
    
    reverse([]) ➞ []

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def reverse(lst):
  return [i for i in lst[::-1]]

