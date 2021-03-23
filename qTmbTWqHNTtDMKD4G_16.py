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
  world = world.split(',')
  world = [world[i:i+width] for i in range(0,len(world),width)]
  for y in range(len(world)):
    for x in range(len(world[y])):
      if world[y][x] == 'm':
        start = [y,x]
        world[y][x] = 0
      elif world[y][x] == 't':
        world[y][x] = -2
      elif world[y][x] == 'h':
        end = [y,x]
        world[y][x] = -1
      else:
        world[y][x] = -1
  val = 0
  y,x = start
  nodes = [[y,x+1],[y,x-1],[y+1,x],[y-1,x],[y+1,x+1],[y+1,x-1],[y-1,x+1],[y-1,x+1]]
  nodes = [i for i in nodes if 0<=i[0]<len(world) and 0<=i[1]<len(world[i[0]]) and world[i[0]][i[1]] != -2]
  while any([world[a][b] == -1 for a,b in nodes]):
    new_nodes = []
    for i in nodes:
      a,b = i
      if world[a][b] == -1:
        world[a][b] = val+1
      new_nodes += [[a,b+1],[a,b-1],[a+1,b],[a-1,b],[a+1,b+1],[a+1,b-1],[a-1,b+1],[a-1,b-1]]
    val+=1
    new_nodes = [i for i in new_nodes if 0<=i[0]<len(world) and 0<=i[1]<len(world[i[0]]) and world[i[0]][i[1]] != -2]
    nodes = []
    for i in new_nodes:
      if i not in nodes:
        nodes.append(i)
  return world[end[0]][end[1]]

