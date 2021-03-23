"""


Create a function that takes four tuples. The first three are (x, y)
coordinates of three corners of a triangle. Return `True` if the fourth tuple
— the (x, y) coordinates of a test point — lies within the triangle, `False`
if it doesn't.

### Examples

    within_triangle((1, 4), (5, 6), (6, 1), (4, 5)) ➞ True
    
    within_triangle((1, 4), (5, 6), (6, 1), (3, 2)) ➞ False
    
    within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)) ➞ True

### Notes

N/A

"""

def solveEquation(p1, p2):
    den = p2[0] - p1[0]
    if(den == 0):
        return (1000000000, 0)
    m = (p2[1] - p1[1]) / den
    b = p2[1] - m * p2[0]
    return (m, b)
​
def getXY(m, b, pt):
    y = (m * pt[0]) + b
    x = (pt[1] - b) / m
    return (x, y)
​
def addToLists(p1, p2, tstPt, lx, ly):
​
    #print("\n\n")
    
    # Compute m, b for y = mx + b
    m, b = solveEquation(p1, p2)
    #print('m {} b {}'.format(m, b))
​
    # Solve for x given y and y given x of y = mx + b
    x, y = getXY(m, b, tstPt)
    #print('X {} Y {}'.format(x, y))
    
    rngX = []
    rngY = []
    rngX.extend([p1[0], p2[0]])
    rngY.extend([p1[1], p2[1]])
    rngX.sort()
    rngY.sort()
​
    xt = tstPt[0]
    yt = tstPt[1]
    
    if((xt >= rngX[0]) and (xt <= rngX[1])):
        #print('P1 {} P2 {} YY {}'.format(p1, p2, y))
        ly.append(y)
    
    if((yt >= rngY[0]) and (yt <= rngY[1])):
        #print('P1 {} P2 {} XX {}'.format(p1, p2, x))
        lx.append(x)
​
    #print('RANGES X {} Y {} LX {} LY {}'.format(rngX, rngY, lx, ly))
​
def addToLists(p1, p2, tstPt, lx, ly):
​
    #print("\n\n")
    
    # Compute m, b for y = mx + b
    m, b = solveEquation(p1, p2)
    #print('m {} b {}'.format(m, b))
​
    # Solve for x given y and y given x of y = mx + b
    x, y = getXY(m, b, tstPt)
    #print('X {} Y {}'.format(x, y))
    
    rngX = []
    rngY = []
    rngX.extend([p1[0], p2[0]])
    rngY.extend([p1[1], p2[1]])
    rngX.sort()
    rngY.sort()
​
    xt = tstPt[0]
    yt = tstPt[1]
    
    if((xt >= rngX[0]) and (xt <= rngX[1])):
        #print('P1 {} P2 {} YY {}'.format(p1, p2, y))
        ly.append(y)
    
    if((yt >= rngY[0]) and (yt <= rngY[1])):
        #print('P1 {} P2 {} XX {}'.format(p1, p2, x))
        lx.append(x)
​
    #print('RANGES X {} Y {} LX {} LY {}'.format(rngX, rngY, lx, ly))
​
def within_triangle(p1, p2, p3, test):
​
    lx = []
    ly = []
    addToLists(p1, p2, test, lx, ly)
    addToLists(p2, p3, test, lx, ly)
    addToLists(p3, p1, test, lx, ly)
    if((len(lx) < 2) or (len(ly) < 2)):
        return False
    lx.sort()
    lx = [lx[0], lx[-1]]
    ly.sort()
    ly = [ly[0], ly[-1]]
    #print('\n\nRNG X {} RNG Y {}'.format(lx, ly))
​
​
    x = test[0]
    y = test[1]
​
    if((x < lx[0]) or (x > lx[1])):
        return False
    if((y < ly[0]) or (y > ly[1])):
        return False
​
    return True

