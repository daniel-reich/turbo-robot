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
  def is_street(lst, column):
    for row in lst:
      if row[column] == '#':
        return False
    return True
  streets = [
    is_street(lst, index)
    for index, column in enumerate(lst[0])
  ]
  result = []
  for row in lst:
    cur_row = []
    for column, street in zip(row, streets):
      if column == ' ' and street:
        cur_row.append(' ' * (n - 1))
      cur_row.append(column)
    result.append(''.join(cur_row))
  return result

