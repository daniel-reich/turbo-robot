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
  lst = lst[1:-1]
  NL = ''
  for i in lst:
    NL += i
  if ' ' in NL:
    return False
  else:
    return True

