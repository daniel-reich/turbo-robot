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
  ans = []
  row_len = 2*h-1
  for i in range(1, row_len+1, 2):
    n = (row_len - i)//2
    row = ' '*n + '#'*i + ' '*n
    ans.append(row)
  return ans

