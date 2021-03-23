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
    return ['#']
  return ['#'*n] + ['#' + ' ' * (n-2) + '#'] * (n-2) + ['#'*n]

