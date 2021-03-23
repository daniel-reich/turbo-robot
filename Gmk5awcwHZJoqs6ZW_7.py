"""


An **island is a region of contiguous ones**. A contiguous one is a `1` that
is touched by at least one other `1`, either **horizontally** , **vertically**
or **diagonally**. Given a piece of the map, represented by a 2-D list, create
a function that returns the area of the largest island.

To illustrate, if we were given the following piece of the map, we should
return `4`.

    [
      [0, 0, 0],
      [0, 1, 1],
      [0, 1, 1]
    ]

Our function should yield `2` for the map below:

    [
      [1, 0, 0],
      [0, 0, 1],
      [0, 0, 1]
    ]

Our function should yield `4` for the map below: :

    [
      [1, 0, 0],
      [0, 1, 1],
      [0, 0, 1]
    ]

### Examples

    largest_island([
      [1, 0, 0], 
      [0, 0, 0], 
      [0, 0, 1]
    ])
    
    ➞ 1
    
    largest_island([
      [1, 1, 0], 
      [0, 1, 1], 
      [0, 0, 1]
    ])
    
    ➞ 5
    
    largest_island([
      [1, 0, 0], 
      [1, 0, 0], 
      [1, 0, 1]
    ])
    
    ➞ 3

### Notes

  * Maps can be any `m x n` dimension.
  * Maps will always have at least 1 element. `m >= 1` and `n >= 1`.

"""

def largest_island(lst):
  moves=[(1,0),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1),(1,1)]
  island, has_ones=0, False
  y=[i for i in range(len(lst))]
  x=[i for i in range(len(lst[0]))]
  for i in range (len(lst)):
    for j in range (len(lst[0])):
      if (lst[i][j]==1):
        has_ones=True
        for move in moves:
          if (i+move[0] in y and j+move[1] in x):
            if(lst[i+move[0]][j+move[1]]==1):
              island+=1
              break
  if has_ones:
    if island ==0:
      return 1
    else:
      return island
  else:
      return 0

