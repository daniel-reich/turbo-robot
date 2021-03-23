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
    homeNode = None
    worldList = loadWorld(world, width, height)
    unvisited = []
    for row in worldList:
        for elem in row:
            unvisited.append(elem)
    
    while len(unvisited) > 0:
        currentNode = minDistance(unvisited)
​
        if currentNode.node_type == 'h':
            homeNode = currentNode
        
        nextNodes = neighbours(worldList, currentNode.coordX, currentNode.coordY)
        
        for elem in nextNodes:
            newDist = currentNode.distance
            newDist = newDist + 1 if elem.node_type != 't' else newDist + 999
            if elem.distance > newDist:
                elem.distance = newDist
        
        unvisited.remove(currentNode)
        
    return -1 if homeNode.distance > 899 else homeNode.distance
  
  
  
def minDistance(unvisited):
    minNode = unvisited[0]
    minDist = unvisited[0].distance
    for node in unvisited:
        if node.distance < minDist:
            minNode = node
            minDist = node.distance    
    return minNode
  
  
  
def neighbours(worldList, coordX, coordY):
    h = len(worldList)
    w = len(worldList[0])
    
    neighbourList = []
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            if coordX + i < w and coordX + i > -1: 
                if coordY + j < h and coordY + j > -1:
                    if i != 0 or j != 0:
                        neighbourList.append(worldList[coordY + j][coordX + i])
    
    return neighbourList
  
  
  
def loadWorld(world, w, h):
    worldList = [[]]
    i = 0
    j = 0
    
    for c in world:
        if c != ',':
            dist = 0 if c == 'm' else 999
            if i == w:
                i = 0
                j += 1
                worldList.append([])
            n = Node(c, dist, i, j)
            i = i + 1
            worldList[j].append(n)
    
    return worldList
  
  
  
class Node:
    
    def __init__ (self, node_type, distance, coordX, coordY):
        self.node_type = node_type
        self.distance = distance
        self.coordX = coordX
        self.coordY = coordY

