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

import numpy as np
import itertools
​
inf = float("inf")
# nan = np.nan
​
​
class Grid():
    def __init__(self, world, width, height):
        self.originalGraph = np.array(world.split(","), dtype=object).reshape(height, width)
        self.graph, self.start, self.goal = self.preprocess(self.originalGraph)
        self.unvisited = set(zip(*np.where(self.graph == inf)))
        self.unvisited.add(self.start)
        self.activelist = set([self.start])
        self.pathLength = self.djkstra(self.start)
​
    @staticmethod
    def preprocess(A):
        start = next(zip(*np.where(A == "m")))
        goal = next(zip(*np.where(A == "h")))
        A[goal] = A[A == "."] = inf
        A[start] = 0
        return A, start, goal
​
    @staticmethod
    def surrounding(A, node):
        ranges = list(list(range(max(n - 1, 0), min(n + 2, r))) for n, r in zip(node, A.shape))
        return set(itertools.product(*ranges))
​
    def djkstra(self, activenode):
        if activenode != self.goal:
            self.unvisited.remove(activenode)
            look = set()
            for x in self.surrounding(self.graph, activenode):
                if x != "t" and x in self.unvisited:
                    look.add(x)
                    self.activelist.add(x)
            self.activelist.remove(activenode)
            if not self.activelist:
                return -1
            else:
                for x in look:
                    self.graph[x] = min(self.graph[x], self.graph[activenode] + 1)
                activenode = min((x for x in self.activelist), key=lambda x: self.graph[x])
                return self.djkstra(activenode)
​
        else:
            return self.graph[self.goal]
​
def get_path_length(world, width, height):
    test = Grid(world, width, height)
    return test.pathLength

