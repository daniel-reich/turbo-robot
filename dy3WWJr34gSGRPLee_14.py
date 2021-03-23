"""


Create a function that creates a box based on dimension `n`.

### Examples

    make_box(5) ➞ [
      "#####",
      "#   #",
      "#   #",
      "#   #",
      "#####"
    ]
    
    make_box(3) ➞ [
      "###",
      "# #",
      "###"
    ]
    
    make_box(2) ➞ [
      "##",
      "##"
    ]
    
    make_box(1) ➞ [
      "#"
    ]

### Notes

N/A

"""

def makeBox(n):
  if n == 1:
    return ["#"]
  
  topbot, middle, box = "", "", []
  for i in range(n):
    topbot += "#"
  
  middle += "#"
  for j in range(n-2):
    middle += " "
  middle += "#"
  
  box = [topbot]
  for k in range(n-2):
    box += [middle]
  box += [topbot]
  return box

