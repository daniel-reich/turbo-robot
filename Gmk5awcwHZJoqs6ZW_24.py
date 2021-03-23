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
  def search(a,b):
    for i in range (len(lst)):
      for j in range (len(lst[0])):
        if lst[i][j]==a:
          lst[i][j] = b
          return [i,j]
    return False
  def check_adjacent(coordinates):
    x,y = coordinates[0],coordinates[1]
    for d in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
      if -1 < x+d[0] < len(lst) and -1 < y+d[1] < len(lst[0]) and lst[x+d[0]][y+d[1]]==1:
        lst[x+d[0]][y+d[1]] = n
  n = 2
  while search(1,1)!=False:
    check_adjacent(search(1,n+1))
    while search(n,n)!=False:
      check_adjacent(search(n,n+1))
    n += 2
  islands = [i for j in lst for i in j if i!=0]
  return max(islands.count(i) for i in islands)

