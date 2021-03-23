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
    brojac = 0
    for i in lst:
        for j in i:
            if(j == " "):
                brojac+=1
    res = False            
    if(brojac == 0):
        res=True
    else:
        res = False
    return res;

