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

import numpy 
​
def exit_maze(maze, directions):
​
  #find starting position, assuming it is unique
  maze_arr=numpy.array(maze)
  r,c=numpy.where(maze_arr==2)
  row_start=numpy.asscalar(r)
  col_start=numpy.asscalar(c)
  row_start=9
  col_start=8
​
  for i in range(len(directions)):
    d = directions[i]
    
    if (d=="N"):
      row_start-=1
      if (row_start>9 or row_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
​
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"
​
​
    if (d=="S"):
      row_start+=1
      
      if (row_start>9 or row_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"
​
​
    if (d=="E"):
      col_start+=1
      
      if (col_start>9 or col_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
      
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"
​
​
    if (d=="W"):
      col_start-=1
      if (col_start>9 or col_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
​
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"

