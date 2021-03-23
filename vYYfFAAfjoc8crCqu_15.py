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
 tree_lst=[]
 tree=[]
 width=(h*2)-1
 h_count=1
 for i in range(0,h):
  # number of hashtags, starting at 1 - iterate +2
  tree_lst.clear()
  # white space each side = width - hashtags  // 2
  wsp=(width-h_count)//2
  # add wsp + hashes + wsp to current str
  #print(' '*wsp+('#'*h_count)+' '*wsp)
  tree.append(' '*wsp+('#'*h_count)+' '*wsp)
  h_count+=2
 return tree

