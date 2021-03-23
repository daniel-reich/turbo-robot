"""


A wristband can have 4 patterns:

  1. **horizontal** : each item in a row is identical.
  2.  **vertical** : each item in each column is identical.
  3.  **diagonal left** : each item is identical to the one on it's upper left or bottom right.
  4.  **diagonal right** : each item is identical to the one on it's upper right or bottom left.

You are shown an **incomplete section** of a wristband.

Write a function that returns `True` if the section can be correctly
classified into one of the 4 types, and `False` otherwise.

### Examples

    is_wristband([
      ["A", "A"],
      ["B", "B"],
      ["C", "C"]
    ]) ➞ True 
    # Part of horizontal wristband.
    
    is_wristband([
      ["A", "B"],
      ["A", "B"],
      ["A", "B"]
    ]) ➞ True 
    # Part of vertical wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["C", "A", "B"],
      ["B", "C", "A"],
      ["A", "B", "C"]
    ]) ➞ True
    # Part of diagonal left wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["B", "C", "A"],
      ["C", "A", "B"],
      ["A", "B", "A"]
    ]) ➞ True
    # Part of diagonal right wristband.

### Notes

N/A

"""

# note: I like working with rows rather than columns
#       hence all the transposing.
def is_wristband(lst):
    if test_rows(lst):      return True
    tlst = map(list, zip(*lst))
    if test_rows(tlst):     return True
    s = slide(lst, -1)
    ts = map(list, zip(*s))
    if test_rows(ts):       return True
    s = slide(lst, 1)
    ts = map(list, zip(*s))
    if test_rows(ts):       return True
    return False
​
def test_rows(arr):
    for row in arr:
        if len(set(x for x in row if x)) != 1:
            return False
    return True
​
# create new array with input diagonal entris aligned
# in columns in output array based on value of di
def slide(arr, di):
    cols = len(arr[0]) + len(arr) - 1
    s = []
    if di == -1:
        i = cols - len(arr[0])
    else:
        i = 0
    for row in arr:
        r = [None] * cols
        r[i:i+len(row)] = row
        s.append(r)
        i += di
    return s

