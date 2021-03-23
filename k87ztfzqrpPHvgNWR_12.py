"""


Given a list of strings _depicting a row of buildings_ , create a function
which **sets the gap between buildings** as a given amount.

### Examples

    widen_streets([
      "###   ## #",
      "### # ## #",
      "### # ## #",
      "### # ## #",
      "### # ## #"
    ], 3) ➞
    [
      "###       ##   #",
      "###   #   ##   #",
      "###   #   ##   #",
      "###   #   ##   #",
      "###   #   ##   #"
    ]
    
    widen_streets([
      "## ### ###",
      "## ### ###",
      "## ### ###",
      "## ### ###"
    ], 2) ➞
    [
      "##  ###  ###",
      "##  ###  ###",
      "##  ###  ###",
      "##  ###  ###"
    ]
    
    widen_streets([
      "# # # # #"
    ], 2) ➞
    [
      "#  #  #  #  #"
    ]

### Notes

  * Buildings may be different sizes.
  * There will always be a starting gap size of **one character**.

"""

def widen_streets(lst, n):
    new = ['']*len(lst)
    for i in range(len(lst)):
        for ind,j in enumerate(lst[i]):
            if lst[-1][ind]=='#': new[i]+=j
            else: new[i]+=' '*n
​
    return new

