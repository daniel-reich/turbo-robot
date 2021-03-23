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
  lst = []
  t = n
  while n >= 1:
    if 1 < n < t:
      lst.append("#" + " " * (t-2) + "#")
      n -=1
    else:
      lst.append("#" * t)
      n -= 1
  return lst

