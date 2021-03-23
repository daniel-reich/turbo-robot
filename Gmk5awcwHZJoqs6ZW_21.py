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
    offsets = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    rows, cols = len(lst), len(lst[0])
    all_islands = []
    
    while any(1 in x for x in lst):
        for i in range(rows):
            for j in range(cols):
                if lst[i][j] == 1:
                    visited = set()
                    stack = [(i, j)]
                    while stack:
                        i, j = stack.pop()
                        if (i, j) not in visited and lst[i][j] == 1:
                            visited.add((i, j))
                            for r, c in offsets:
                                if 0 <= i+r < rows and 0 <= j+c < cols: 
                                    stack.append((i+r, j+c))
                    all_islands.append(len(visited))
                    for i, j in visited:
                        lst[i][j] = 0
            
    return sorted(all_islands)[-1]

