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

tree = lambda h: [' ' * (((h*2-1)-x)//2) + '#' * x +
  ' ' * (((h*2-1)-x)//2) for x in [k*2-1 for k in range(1, h+1)]]

