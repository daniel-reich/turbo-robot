"""


Write a function that takes three arguments `(x, y, z)` and returns a list
containing `x` sublists (e.g. `[[], [], []]`), each containing `y` number of
item `z`.

  * `x` Number of sublists contained within the main list.
  * `y` Number of items contained within each sublist.
  * `z` Item contained within each sublist.

### Examples

    matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
    
    matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
    
    matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]

### Notes

  * The first two arguments will always be integers.
  * The third argument is either a string or an integer.

"""

def matrix(x, y, z):
  list1 = []
  i = 0
  while i < x:
    list1.insert(i, [z]*y)
    i += 1
  return list1

