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
  if n==1:
    return ["#"]
  num_itr = n - 2
  box = ["#"*n]
  for itr in range(num_itr):
    box.append("#"+" "*num_itr+"#")
  box.append("#"*n)
  return box

