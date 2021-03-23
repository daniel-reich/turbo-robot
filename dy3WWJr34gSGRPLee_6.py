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

c="#"
makeBox=lambda n:[c*n]+[c+" "*(n-2)+c]*(n-2)+[c*n]*(n>1)

