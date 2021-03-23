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
  l = len(lst)
  w = len(lst[0])
  print(l, w)
  for i in range(1,l-1):
    for j in range(1,w-1):
      if lst[i][j] == '*':
        return True
  return False

