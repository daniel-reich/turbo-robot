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
    lst = []
    top = '#' * n
    mid = '#' + (n-2)*' ' + '#'
    lst.append(top)
    for x in range(n-2):
        lst.append(mid)
    lst.append(top)
    return lst

