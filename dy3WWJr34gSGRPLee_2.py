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
    a = []
    for i in range(n):
        if i == (n-1) or i == 0: 
            a.append(n*"#")
        else:
            a.append("#" + (n-2)*(" ")+ "#")
    return a

