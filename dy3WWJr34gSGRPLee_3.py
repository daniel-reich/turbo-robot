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
    for i in range(1,n+1):
        if i == 1 or i == n:
            a.append("#"*n)
        elif 1<i<n:
            a.append("#"+" "*(n-2)+"#")
    return a

