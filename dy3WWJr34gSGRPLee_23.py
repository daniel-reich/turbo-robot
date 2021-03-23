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
  arr = []
  strr = ""
  if n == 1:
      arr.insert(0,"#")
  else:
      arr.insert(0,"#"*n)
      for i in range(1,n-1):
          strr = ""
          strr = strr + "#" + (" "*(n-2)) + "#"
          arr.insert(i,strr)
      arr.insert(n,"#"*n)
  return arr

