"""


This is a sequel to [Chain Reaction (Part
#1)](https://edabit.com/challenge/bf3QRDxH9Ns2SZWZw), with the same setup, but
a different flavor.

As in the previous part, you will be given a rectangular array representing a
"map" with three types of spaces:

  * "+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  * "x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

The goal is simple: **given a map, return the minimum number of bombs that
need to be set off for all bombs to be destroyed by the chain reaction**.

Let's look at some examples:

    [
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]

For the map above, the answer is `2`; to explode all bombs you just need to
set off one "+" bomb in the right cluster and one in the left cluster.

    [
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]

For the map above, the answer is `3`; clearly setting off the three bottom "x"
bombs is enough, and no less than three bombs suffice.

    [
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]

For the map above, the answer is `3`; setting off the three rightmost bombs in
the middle row will do the trick.

### Examples

    min_bombs_needed([
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]) ➞ 2
    
    min_bombs_needed([
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]) ➞ 3
    
    min_bombs_needed([
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]) ➞ 3

### Notes

  * Note that both "+" and "x" bombs have an "explosion range" of 1.
  * To limit the difficulty, in this challenge each map will have only "+" or only "x" bombs. The more challenging case of maps with both "+" and "x" bombs will be [part 3](https://edabit.com/challenge/LLieA2XafALFxXRT5)!
  * Figuring out what to do is half the fun, but if you'd prefer to just handle the coding, a hint on to how to attack this challenge can be found in the comments.

"""

def min_bombs_needed (bombs_grid):
    '''
    Returns the minimum number of bombs needed to explode all the bombs.
    '''
    def bomb_neighbours(grid, i, j):
        '''
        Returns the neighbours of bomb grid[i][j] which will explode based
        on its bomb type if it is a bomb and explodes.
        '''
        bomb = grid[i][j]
        if bomb == '0':
            return []  # not a bomb
        
        all_neighbours = [(r,c) for r in range(max(0,i-1),min(len(grid),i+2))\
                          for c in range(max(0,j-1),min(len(grid[0]),j+2)) if grid[r][c] != '0' \
                          and not(i==r and j==c)]
        
        if bomb == '+':
            return [(b,c) for b,c in all_neighbours if b==i and c==j-1 or b==i and c==j+1 \
                    or b==i-1 and j==c or b==i+1 and j==c]  # bomb neighbours of '+' bomb
        return [(b,c) for b,c in all_neighbours if b==i-1 and c==j-1 or b==i-1 and c==j+1\
                    or b==i+1 and c==j-1 or b==i+1 and c==j+1] # bomb neighbours of 'x' bomb
​
    def exploded_bombs(grid, i, j, exploded):
        '''
        Updates exploded with any bombs not already exploded as a result of the bomb
        at grid[i][j] exploding.
        '''
        q = []
        q.append((i,j))
​
        while q:
            i, j = q.pop(0)   # get nearest bomb and its position
            exploded.add((i,j))
        
            for r, c in bomb_neighbours(grid, i, j):
                if (r,c) not in exploded:
                    q.append((r,c))
        
    exploded = set()
    count = 0
    
    for i in range(len(bombs_grid)):
        for j in range(len(bombs_grid[0])):
            if bombs_grid[i][j] != '0' and (i,j) not in exploded:
                exploded_bombs(bombs_grid,i,j,exploded)
                count += 1
​
    return count

