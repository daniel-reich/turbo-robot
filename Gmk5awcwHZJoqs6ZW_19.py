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
    def ones_position(lst):
        positions = []
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if lst[i][j] == 1:
                    positions.append((i,j))
        return positions
    def connected(p,q):
        d1 = abs(p[0]-q[0])
        d2 = abs(p[1]-q[1])
        return d1 <1.5 and d2<1.5
    def pairwise_connected(positions):
        connect_mat = []
        for i,p in enumerate(positions):
            l = []
            for j,q in enumerate(positions):
                l.append(connected(p,q))
            connect_mat.append(l)
        return connect_mat
    positions = ones_position(lst)
    conn_mat = pairwise_connected(positions)
    return max(list(map(sum,conn_mat)))

