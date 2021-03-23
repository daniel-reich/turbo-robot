"""


It's been a long day for Matt. After working on Edabit for quite a bit, he
decided to go out and get a beer at the local bar a few miles down the road.
However, what Matt didn't realise, was that with too much drinks you can't
find the way home properly anymore. Your goal is to help Matt get back home by
telling him how long the path to his house is if he drives the optimal route.

Matt lives in a simple world: there is only dirt (represented by a dot), a
single house (Matt's house, represented by the letter "h") and there are trees
(represented by the letter "t") which he obviously can't drive through. Matt
has an unlimited amount of moves and each move he can go north, north-east,
east, south-east, south, south-west, west and north-west. There will only be
one Matt and one house, which is Matt's.

The world is given to you as a comma-delimited string which represents the
cells in the world from top-left to bottom-right. A 3x3 world with Matt on the
top-left and his house on the bottom-right, with a tree in the middle would be
represented as:

    m,.,.,.,t,.,.,.,h

The answer to this world would be 3: Matt would first move east, then south-
east, then south (or south > south-east > east). The function call related to
this example would be the following:

    get_path_length("m,.,.,.,t,.,.,.,h", 3, 3)

If Matt is unable to get home from his current location, return `-1`,
otherwise return the amount of moves Matt has to make to get home if he
follows the optimal path. You are given the world, it's width and it's height.

 **Good luck!**

"""

def get_path_length(world, width, height):
  world = [world.split(',')[row*width:(row+1)*width] for row in range(height)]
  step_count = [[0 for step in world] for row in world]
  if height == 1:
    return len(world[0]) - 1
    
  def start(li, li2):
    for i in range(len(li)):
      for j in range(len(li[i])):
        if li[i][j] == 'm':
          return [i,j]
​
  def end(li, li2):
    for i in range(len(li)):
      for j in range(len(li[i])):
        if li[i][j] == 'h':
          return [i,j]
  
  matt = start(world, step_count)
  house = end(world, step_count)
  count_of_zeros = 0
  
  def move(range1, range2):
    for i in range1:
      for j in range2:
        if world[row+i][col+j] == 't':
          continue
        elif step_count[row+i][col+j] != 0 and step_count[row+i][col+j] < step_count[row][col] + 1:
          continue
        else:
          step_count[row+i][col+j] = step_count[row][col] + 1
          
  while step_count[house[0]][house[1]] == 0:
    step_count[matt[0]][matt[1]] = 1
    zeros = []
    for row in range(len(world)):
      for col in range(len(world[0])):
        if step_count[row][col] == 0:
          zeros.append(step_count[row][col])
        elif row == 0 and col == 0:
          move((0,1), (0,1))
        elif row == 0 and col != len(world[0]) - 1:
          move((0,1), (-1,0,1))
        elif row == 0 and col == len(world[0]) - 1:
          move((0,1), (-1,0))
        elif row != 0 and row != len(world) - 1 and col == 0:
          move((-1,0,1), (0,1))
        elif row == len(world) - 1 and col == 0:
          move((-1,0), (0,1))
        elif row == len(world) - 1 and col != 0 and col != len(world[0]) - 1:
          move((-1,0), (-1,0,1))
        elif row == len(world) - 1 and col == len(world[0]) - 1:
          move((-1,0), (-1,0))
        elif row != len(world) - 1 and col == len(world[0]) - 1:
          move((-1,0,1), (-1,0))
        else:
          move((-1,0,1), (-1,0,1))
    if len(zeros) == count_of_zeros:
      break
    else:
      count_of_zeros = len(zeros)
  return step_count[house[0]][house[1]] -1

