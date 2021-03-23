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
  flag = False
  for item in lst[1:-1]:
    if '*' in item[1:-1]:
      flag = True
      break
  return flag

