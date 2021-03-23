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
    mat =  [world[idx:(idx+width)] for idx in range(0,height*width-1, height)]
    start = world.index('m')//width, world.index('m')%width
    goal = world.index('h')//width, world.index('h')%width
    current_level, visited = {start}, set()
​
    def neighbors(y,x):
        def can_go(y_,x_):
            return 0<=y_<height and 0<=x_<width and mat[y_][x_]!='t'
        directions = [(-1,-1),(-1, 0),(-1, 1),( 0,-1),
                      ( 0, 1),( 1,-1),( 1, 0),( 1, 1),]
        return [(y+dy, x+dx) for dy, dx in directions if can_go(y+dy, x+dx)]
​
    depth = 0
    while current_level:
        if goal in current_level:
            return depth
        current_level = {n for pos in current_level for n in neighbors(*pos)} - visited
        visited.update(current_level)
        depth += 1
    return -1

