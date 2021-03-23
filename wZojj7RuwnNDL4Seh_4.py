"""


Create a function that checks if the box is completely filled with the
asterisk symbol `*`.

### Examples

    completely_filled([
      "#####",
      "#***#",
      "#***#",
      "#***#",
      "#####"
    ]) ➞ True
    
    completely_filled([
      "#####",
      "#* *#",
      "#***#",
      "#***#",
      "#####"
    ]) ➞ False
    
    completely_filled([
      "###",
      "#*#",
      "###"
    ]) ➞ True
    
    completely_filled([
      "##",
      "##"
    ]) ➞ True

### Notes

Boxes of size `n <= 2` are considered automatically filled (see example #4).

"""

def completely_filled(lst):
  if len(lst) <= 2:
    return True
  for i in range(0, len(lst) - 2):
    for j in range(0, len(lst[i]) - 2):
      if lst[i+1][j+1] != '*':
        return False
  return True

