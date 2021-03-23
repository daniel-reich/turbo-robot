"""


Write a function to create a Christmas tree based on height `h`.

### Examples

    tree(1) ➞ [
      "#"
    ]
    
    tree(2) ➞ [
      " # ",
      "###"
    ]
    
    tree(5) ➞ [
      "    #    ",
      "   ###   ",
      "  #####  ",
      " ####### ",
      "#########"
    ]
    
    tree(0) ➞ []

### Notes

N/A

"""

def tree(h):
  L = []
  for i in range(1,h*2,2):
    L.append("#" * i)
  FL = []
  for i in range(len(L)):
    FL.append(" "*(h-i-1) + L[i] + " "*(h-i-1))
  return FL

