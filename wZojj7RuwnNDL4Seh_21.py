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
  return all([True if " " not in l else False for ls in lst[1:-1] for l in ls[1:-1]])

