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
    islands, m, n = [], len(lst), len(lst[0])
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1:
                if not islands:
                    islands.append([[i, j]])
                else:
                    touch_an_island = False
                    for island in islands:
                        touch = False
                        for dot in island:
                            if abs(dot[0] - i) < 2 and abs(dot[1] - j) < 2:
                                touch = True
                                break
                        if touch:
                            island.append([i, j])
                            touch_an_island = True
                            break
                    if not touch_an_island:
                        islands.append([[i, j]])
    return max(len(island) for island in islands)

