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

def make_box(s):
  n = [("#"*s) for i in range(s)]
  n = [k if i == 0 or i == s-1 else "{}".format("#"+" "*(s-2)+"#") for i,k in enumerate(n)]
  return n

