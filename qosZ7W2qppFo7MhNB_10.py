"""


A **hexagonal grid** is a commonly used **game board design** based on
hexagonal tiling. In the following grid, the two marked locations have a
minimum distance of 6 because at least 6 steps are needed to reach the second
location starting from the first one.

![](https://edabit-challenges.s3.amazonaws.com/HiD.svg)

Write a function that takes a hexagonal grid with two marked locations as
input and returns their distance.

The input grid will be a list of strings in which each tile is represented
with `o` and the two marked locations with `x`.

### Examples

    hex_distance([
      "  o o  ",
      " o x o ",
      "  o x  ",
    ]) ➞ 1
    
    hex_distance([
      "  o o  ",
      " x o o ",
      "  o x  ",
    ]) ➞ 2
    
    hex_distance([
      "   o o o   ",
      "  o o o o  ",
      " o o o o o ",
      "  x o o x  ",
      "   o o o   ",
    ]) ➞ 3

### Notes

N/A

"""

def hex_tiles(tiles,loc):
    '''
    Returns the addresses of the tiles which are adjacent to the tile at loc.
    '''
    i, j = loc
    possibles = ((i-1,j-1),(i-1,j+1),(i,j-2),
                 (i,j+2),(i+1,j-1),(i+1,j+1))
    return [(a,b) for a, b in possibles if 0 <= a < len(tiles) and \
            0 <= b < len(tiles[0]) and tiles[a][b] != ' ']
​
def count_steps(start, end, tiles):
    '''
    Returns the minimum number of steps between tile start and tile end
    '''
    q = [start]
    visited = set()
    prev = [[-1 for j in range(len(tiles[0]))] for i in range(len(tiles))]
​
    while q:
        tile = q.pop(0)
        if tile == end:
            break
        visited.add(tile)
        for i, j in hex_tiles(tiles, tile):
            if (i,j) not in visited and (i,j) not in q:
                prev[i][j] = (tile[0],tile[1])
                q.append((i,j))
​
    count = 0
    next_tile = end
    while next_tile != start:
        count += 1
        next_tile = prev[next_tile[0]][next_tile[1]]
​
    return count
​
def hex_distance(tiles):
    '''
    Returns the shortest distance between the 2 tiles in tiles marked 'x' as
    per instructions.
    '''
    x1, x2 = [(i,j) for i in range(len(tiles)) for j in range(len(tiles[0])) \
              if tiles[i][j] == 'x']
    return count_steps(x1, x2, tiles)

