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
  def standardize_building_sizes(lst):
    cols = {}
​
    for n in range(len(lst[0])):
      col = ''
      for row in lst:
        col += row[n]
      cols[n] = col
​
    max_height = len(lst)
    hash_cols = {}
​
    for col in cols.values():
      hash_cols[col] = col.count('#')
    
    new_cols = {}
​
    for n in cols.keys():
      if hash_cols[cols[n]] < max(hash_cols.values()) and hash_cols[cols[n]] != 0:
        hashes = '#' * hash_cols[cols[n]]
        space_fillers = '%' * (max(hash_cols.values()) - hash_cols[cols[n]])
        spaces = ' ' * (max_height - max(hash_cols.values()))
        new_col = spaces + space_fillers + hashes
        new_cols[n] = new_col
      else:
        new_cols[n] = cols[n]
    
    new_grid = []
    
    for n in range(max_height):
      row = ''
      for col_id in sorted(list(new_cols.keys())):
        col = new_cols[col_id]
        row += col[n]
      new_grid.append(row)
    
    return new_grid
  def widen(lst, gap):
    new_grid = []
​
    for n in range(len(lst)):
      row = lst[n].replace(' ', ' ' * gap)
      new_grid.append(row)
    
    return new_grid
  def destandardize_building_sizes(lst):
​
    new_grid = []
​
    for n in range(len(lst)):
      row = lst[n].replace('%', ' ')
      new_grid.append(row)
    
    return new_grid
​
  sbs = standardize_building_sizes(lst)
  new = widen(sbs, n)
  dbs = destandardize_building_sizes(new)
​
  return dbs

