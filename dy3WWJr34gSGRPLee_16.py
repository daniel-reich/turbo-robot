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
    c1 = ''.join(['#' for i in range(n)])
    c2 = ''.join(['#' if (i == 0 or i == n-1) else ' ' for i in range(n)])
    c3 = [c1 if (i == 0 or i == n-1) else c2 for i in range(n)]
    return c3

