"""


Create a function that takes a list of numbers `lst` and returns an **inverted
list**.

### Examples

    invert_list([1, 2, 3, 4, 5]) ➞ [-1, -2, -3, -4, -5]
    
    invert_list([1, -2, 3, -4, 5]) ➞ [-1, 2, -3, 4, -5]
    
    invert_list([]) ➞ []

### Notes

  * Don't forget to return the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def invert_list(arr):
  arr2 = []
  arr3 = 0
  for i in arr:
    arr3 = - i
    arr2.append(arr3)
  return arr2

