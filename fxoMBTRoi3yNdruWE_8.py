"""


Create a function that returns `True` if an asterisk `*` is inside a box.

### Examples

    in_box([
      "###",
      "#*#",
      "###"
    ]) ➞ True
    in_box([
      "####",
      "#* #",
      "#  #",
      "####"
    ]) ➞ True
    in_box([
      "*####",
      "# #",
      "#  #*",
      "####"
    ]) ➞ false
    in_box([
      "#####",
      "#   #",
      "#   #",
      "#   #",
      "#####"
    ]) ➞ False

### Notes

The asterisk may be in the array, however, it must be inside the box, if it
exists.

"""

def in_box(lst):
  for row in lst:
    if"*"in row and"*"not in row[0]and"*"not in row[-1]:
      return True
  return False

