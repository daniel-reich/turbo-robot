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
    lst_w = world.split(',')
    lst_2d = []
    for r in range(height):
        lst_2d.append(lst_w[:width])
        lst_w = lst_w[width:]
    all_dots = set()
    for r in range(height):
        for c in range(width):
            if lst_2d[r][c] == '.':
                all_dots.add((r, c))
            elif lst_2d[r][c] == 'm':
                start = (r, c)
            elif lst_2d[r][c] == 'h':
                finish = (r, c)
    steps = 0
    link = [start]
    while link:
        new_link = []
        steps += 1
        for pos in link:
            for move in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),
                         (0, -1), (-1, -1)]:
                new_pos = (pos[0] + move[0], pos[1] + move[1])
                if new_pos == finish:
                    return steps
                elif new_pos in all_dots:
                    new_link.append(new_pos)
                    all_dots -= {new_pos}
        link = new_link
    return -1
