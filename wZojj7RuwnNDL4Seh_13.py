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
    return all(' ' not in x[1:-1] if len(lst)>2 else True for x in lst)

