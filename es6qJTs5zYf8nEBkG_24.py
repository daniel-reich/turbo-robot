"""


Create a function that determines whether four coordinates properly create a
rectangle. A rectangle has 4 sides and has 90 degrees for each angle.
Coordinates are given as strings containing an x- and a y- coordinate: `"(x,
y)"`.

For this problem, assume none of the rectangles are tilted.

    is_rectangle(["(0, 0)", "(0, 1)", "(1, 0)", "(1,1)"]) ➞ True

### Examples

    is_rectangle(["(-4, 3)", "(4, 3)", "(4, -3)", "(-4, -3)"]) ➞ True
    
    is_rectangle(["(0, 0)", "(0, 1)"]) ➞ False
    # A line is not a rectangle!
    
    is_rectangle(["(0, 0)", "(0, 1)", "(1, 0)"]) ➞ False
    # Neither is a triangle!
    
    is_rectangle(["(0, 0)", "(9, 0)", "(7, 5)", "(16, 5)"]) ➞ False
    # A parallelogram, but not a rectangle!

### Notes

  * A square is also a rectangle!
  * A parallelogram is NOT necessarily a rectangle (the rectangle is a special case of a parallelogram).
  * If the input is fewer than or greater than 4 coordinates, return `False`.

"""

def convertToNum(point):
  m = len(point)
  xString = ''
  yString = ''
  for n in range(0,m):
    p = point[n]
    if p == ',':
      commaPoint = n
      break
  for i in range(1,commaPoint):
    xString += point[i]
  for j in range(commaPoint+1,m-1):
    yString += point[j]
  xInt = float(xString)
  yInt = float(yString)
  return([xInt,yInt])
  
​
def is_rectangle(list):
​
  numOfPoints = len(list)
  if numOfPoints != 4:
    return(False)
    
  point_1 = convertToNum(list[0])
  point_2 = convertToNum(list[1])
  point_3 = convertToNum(list[2])
  point_4 = convertToNum(list[3])
  
  numList = [(point_1),(point_2),(point_3),(point_4)]
  
  x1 = numList[0][0]
  y1 = numList[0][1]
  
  x1Pair = False
  for i in range(1,4):
    if numList[i][0] == x1:
      y2 = numList[i][1]
      x1Pair = True
    elif numList[i][0] != x1:
      x2 = numList[i][0]
  if x1Pair == False:
    return(False)
​
  for j in range(0,4):
    if numList[j] == [x1,y1] or numList[j] == [x1,y2] or numList[j] == [x2,y1] or numList[j] == [x2,y2]:
      rectangle = True
    else:
      rectangle = False
      break
      
  if numList[0] == numList[1] or numList[0] == numList[2] or numList[0] == numList[3]:
    rectangle = False
  if numList[1] == numList[2] or numList[1] == numList[3]:
    rectangle = False
  if numList[2] == numList[3]:
    rectangle = False
  
  return(rectangle)

