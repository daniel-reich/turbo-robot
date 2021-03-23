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
    visited = set()
    def check(rows, cols):
        if not (0 <= rows < len(lst) and 0 <= cols < len(lst[0]) and (rows, cols) not in visited and lst[rows][cols]):
            return 0
        visited.add((rows, cols))
        return (1 + check(rows+1, cols) + check(rows-1, cols) + check(rows, cols-1) + check(rows, cols+1) + check(rows-1,cols-1) + check(rows+1,cols+1) + check(rows+1,cols-1) + check(rows-1,cols+1))
​
    return max(check(rows, cols)
                for rows in range(len(lst))
                for cols in range(len(lst[0])))

