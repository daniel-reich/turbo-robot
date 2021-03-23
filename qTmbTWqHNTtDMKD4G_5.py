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

class Graph(object):
    def __init__(self, world, width, height):
        self.nodes = {}
        self.world = world.split(',')
        self.width = width
        self.height = height
        
        y = 0
        x = 0
        for node in range(self.height * self.width):
            loc = [y, x]
            self.nodes[node] = Node(node, self.world[node], float('inf'), loc)
            x += 1
            if (node + 1) % (self.width) == 0:
                y += 1
                x = 0
            node += 1
​
        self.grid = self.create_grid()
        self.node_grid = self.create_node_grid()
        
        for node in self.nodes:
            self.nodes[node].neighbors = self.nodes[node].get_neighbors(self.nodes, self.height, self.width, self.node_grid)
​
    def display_graph(self):
        for node in self.nodes:
            print(self.nodes[node])
​
    def get_node_grid(self):
        return self.node_grid
​
    def create_grid(self):
        grid = []
        vertex = 0
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(self.world[vertex])
                vertex += 1
            grid.append(row)
        return grid
​
    def create_node_grid(self):
        grid = []
        node = 0
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(self.nodes[node])
                node += 1
            grid.append(row)
        return grid
​
    def display_grid(self, grid):
        for row in grid:
            print(row)
​
​
class Node(Graph):
    def __init__(self, name, value, cost, node_loc):
        self.name = name
        self.value = value
        self.cost = None
        self.neighbors = None
        self.node_loc = node_loc
        if self.value != 't':
            self.cost = cost
        self.start = False
        self.end = False
        if self.value == 'm':
            self.cost = 0
            self.start = True
        elif self.value == 'h':
            self.end = True
​
    def __repr__(self):
        return 'N' + str(self.name)
​
    def __str__(self):
        return 'Node' + str(self.name) + ' - Loc: ' + str(self.node_loc) + ', Cost: ' + str(self.cost) + ', Value: ' + str(self.value) + ', Start: ' + str(self.start) + ', End: ' + str(self.end) + ', Neighbors: ' + str(self.neighbors)
​
    def get_neighbors(self, nodes, height, width, node_grid):
        neighbors = []
        pot_neighbors = [
            [-1,-1], #NW
            [-1,0], #N
            [-1,1], #NE
            [0,-1], #W
            [0,1], #E
            [1,-1], #SW
            [1,0], #S
            [1,1]] #SE
        y = self.node_loc[0]
        x = self.node_loc[1]
        for each in pot_neighbors:
            if 0 <= each[0] + y <= height * width and 0 <= each[1] + x <= height * width:
                try:
                    if node_grid[each[0] + y][each[1] + x].value != 't':
                        neighbors.append(node_grid[each[0] + y][each[1] + x])
                except IndexError:
                    pass
            if self.value == 't':
                return None
        return neighbors
​
​
def dijkstra(graph, start, end):
    temp_nodes = graph.nodes.copy()
    perm_nodes = {}
    iteration1 = True
    
    while len(temp_nodes) > 0:
        # find temp node with lowest cost to move to
        lowest_cost = float('inf')
        for n in temp_nodes:
            if iteration1:
                lowest_node = temp_nodes[start]
                lowest_cost = lowest_node.cost
                end_node = temp_nodes[end]
            elif temp_nodes[n].cost != None and temp_nodes[n].cost < lowest_cost:
                lowest_cost = temp_nodes[n].cost
                lowest_node = temp_nodes[n]
                
            if lowest_node == end_node:
                return end_node.cost
​
        # make lowest node permanent
        try:
            perm_nodes[lowest_node.name] = temp_nodes.pop(lowest_node.name)
        except KeyError:
            return -1
​
        # remove lowest node from all neighbor lists
        for n in temp_nodes:
            if temp_nodes[n].neighbors != None and temp_nodes[n].neighbors != []:
                for neighbor in temp_nodes[n].neighbors:
                    if neighbor.name in perm_nodes:
                        temp_nodes[n].neighbors.remove(neighbor)
​
        # calculate costs of moving to neighbor nodes
        for n in lowest_node.neighbors:
            if temp_nodes[n.name].cost > lowest_node.cost:
                temp_nodes[n.name].cost = lowest_node.cost + 1
        iteration1 = False
    
​
​
def get_path_length(world, width, height):
    graph = Graph(world, width, height)
    for node in graph.nodes:
        if graph.nodes[node].start == True:
            start = node
        if graph.nodes[node].end == True:
            end = node
    return dijkstra(graph, start, end)

