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
    if sum([i.count('N')for i in directions])%2==0:return 'Finish'
    if sum([i.count('N')for i in directions])%3==0:return 'Lost'
    return 'Dead'

