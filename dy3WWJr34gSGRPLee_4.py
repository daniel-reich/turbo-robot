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
  out = []
  for i in range(n):
    if i == 0 or i == n-1:
      out.append(n*"#")
    else:
      out.append("#"+(n-2)*" "+"#")
  return(out)

