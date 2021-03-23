"""


Given a two-dimensional list of `maze` and a list of `directions`. Your task
is to follow the given directions.

  * If you can reach the endpoint before all your moves have gone, return `"Finish"`.
  * If you hit any walls or go outside the maze border, return `"Dead"`.
  * If you find yourself still in the maze after using all the moves, return `"Lost"`.

The maze list will look like this:

    maze = [
      [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
      [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
      [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
      [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]
    ]
    
    # 0 = Safe place to walk
    # 1 = Wall
    # 2 = Start Point
    # 3 = Finish Point
    # N = North, E = East, W = West and S = South

See the below examples for a better understanding:

### Examples

    exit_maze(maze, ["N", "E", "E"]) ➞ "Dead"
    # Hitting the wall should return "Dead".
    
    exit_maze(maze, ["N", "N", "N", "E"]) ➞ "Lost"
    # Couldn't reach the finish point.
    
    exit_maze(maze, ["N", "W", "W", "W", "N", "N", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N"]) ➞ "Finish"

### Notes

N/A

"""

def exit_maze(maze, directions):
    l = len(maze)
    w = len(maze[0])
    for y in range(l):
        for x in range(w):
            if maze[y][x] == 2:
                sx = x
                sy = y
​
    for i in directions:
        if i == 'N':
            sy -= 1
        elif i == 'E':
            sx += 1
        elif i == 'S':
            sy += 1
        elif i == 'W':
            sx -= 1
        else:
            return 'Bad Direction'
​
        if sy < 0 or sy >= l:
            return 'Dead'
        if sx < 0 or sx >= w:
            return 'Dead'
        if maze[sy][sx] == 1:
            return 'Dead'
        if maze[sy][sx] == 3:
            return 'Finish'
    return 'Lost'

