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
  new_strt = []
  final_str = []
  if len(lst)>1:
    lst.append(' '*len(lst[0]))
    for i in range(len(lst)-1):
      for j in range(len(lst[i])):
        if lst[i][j]==" " and lst[i+1][j]==" ":
          new_strt.append(lst[i][j]*n)
        else:
          new_strt.append(lst[i][j])
      final_str.append("".join(new_strt))
      new_strt.clear()
  else:
    for i in lst:
      final_str.append(i.replace(" "," "*n))
  return final_str

