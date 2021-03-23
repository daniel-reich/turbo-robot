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

def tree(n):
    if n == 0:
         return []
    width = (2 * n) - 1
    output = []
    branch = '#'
    blankwidth = (width - len(branch)) // 2
    for i in range(n):
         output.append((' ' * blankwidth) + branch + (' ' * blankwidth))
         branch += '##'
         blankwidth = (width - len(branch)) // 2
    return output

