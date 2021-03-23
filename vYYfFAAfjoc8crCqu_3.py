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
  try:
    lst = [n for n in range(0,h*2) if n%2!=0]
    w = max(lst)
    return [' '*((w-n)//2)+n*'#'+' '*((w-n)//2) for n in lst]
  except:
    return []

