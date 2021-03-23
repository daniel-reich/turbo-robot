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
  end = "#" * n
  middle = "#" + (" " * (n-2)) + "#"
  box = [end]
  for i in range(2, n):
    box.insert(i, middle) 
  box.append(end)
  return box

