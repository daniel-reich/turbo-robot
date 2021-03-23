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
  pattern = [i for i in range(len(lst[-1])) if lst[-1][i]=='#']
  wide = [''.join(i[j] if j in pattern else ' '*n for j in range(len(lst[0]))) for i in lst]
  return wide

