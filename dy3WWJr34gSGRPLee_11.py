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

def make_box(n):
  box = []
  box.append("#"*n)
  for i in range(n-2):
    box.append("#" + " " * (n-2) + "#")
  
  box.append("#"*n)
  if n == 1: 
    return ["#"]
  else: 
    return box

