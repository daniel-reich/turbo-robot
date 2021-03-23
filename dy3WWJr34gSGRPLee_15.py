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
    lst = []
    if n==1:
        lst.append("#")
    else:
        lst.append("#"*n)
        for i in range(1,n-1):
            lst.append("#"+" "*(n-2)+"#")
            
        lst.append("#"*n) 
    return lst

