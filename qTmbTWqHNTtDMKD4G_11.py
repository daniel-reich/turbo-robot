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

def get_path_length(world,w,h):
    '''
    Returns the shortest route from Matt's position to his home avoiding trees
    as per the instructions.
    '''
​
    def get_locs(world,i,j):
        '''
        Returns a list of the locations in world which can be reached in 1 step
        from world[i][j]
        '''
        locs = ((i,j-1),(i,j+1),(i-1,j-1),(i-1,j),
                (i-1,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
​
        return [(a,b) for a,b in locs if 0<=a<h and 0<=b<w and world[a][b] != 't']
    
    world = world.replace(',','')
    matt, home = world.index('m'), world.index('h')
    matt = (matt//w, matt%w)
    home = (home//w, home%w)  # positions in 2d representation of world
    world = [world[i*w:i*w+w] for i in range(h)]
    
    prev =[[None for loc in row] for row in world] # track Matt's route home
    visited = set()
    q = []
    q.append(matt)  # start from where he is
​
    while q:
        i,j = q.pop(0)
        visited.add((i,j))
        if (i,j) == home:   # made it: shouldn't be driving if he's been drinking though!
            current = prev[home[0]][home[1]]
            count = 0
            while current:
                count += 1
                current = prev[current[0]][current[1]]
​
            return count
​
        for a,b in get_locs(world,i,j):
            if (a,b) not in visited and (a,b) not in q:
                prev[a][b] = (i,j)  # their predecessor
                q.append((a,b))
​
    return -1  # he's trapped by trees!

