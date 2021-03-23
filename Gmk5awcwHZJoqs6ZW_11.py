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
  alreadyPassed = [[0 for i in range(len(lst[0]))] for j in range(len(lst))]
  maxArea = 0
  INCREMENT = 0
  RESET = 1
  GET_VAR = 2
  
  def staticVarManagement(action):
    if action == RESET:
      staticVarManagement.counter = 0
    elif action == INCREMENT:
      staticVarManagement.counter += 1
    return staticVarManagement.counter
  
  def computeArea(x,y):
    if x >= 0 and x < len(lst) and y >= 0 and y < len(lst[0]):
      if alreadyPassed[x][y] == 0 and lst[x][y] == 1:
        staticVarManagement(INCREMENT)
        alreadyPassed[x][y] = 1
        for dx in range(-1,2):
          for dy in range(-1,2):
            computeArea(x+dx,y+dy)
  
  for x,subLst in enumerate(lst):
    for y,elmt in enumerate(subLst):
      staticVarManagement(RESET)
      computeArea(x,y)
      maxArea = max(maxArea,staticVarManagement(GET_VAR))
  return maxArea

