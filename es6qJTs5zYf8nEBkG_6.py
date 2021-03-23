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

def get_slope(pt1,pt2):
  (pt1x , pt1y) = pt1
  (pt2x , pt2y) = pt2
  if (pt2y - pt1y) == 0:
    return 1
  slope = (pt2x - pt1x)/(pt2y - pt1y)
  return slope
​
def is_midpt_90_deg(pt1,pt2,pt3):
  slope1 = get_slope(pt1,pt2)
  slope2 = get_slope(pt2,pt3)
  if slope1 is None or slope2 is None:
    return False
  if  (slope1 == 1 and slope2 == 0)  \
      or (slope1 == 0 and slope2 == 1):
    return True
  if (slope2 != 0 and slope1 == 1/-(slope2)) \
    or (slope1 != 0 and slope2 == 1/-(slope1)):
    return True
  return False
​
def getPoint(value):
  try:
    pt_temp = value.replace("(","") \
                      .replace(")","")  \
                      .replace(" ","") \
                      .split(',')
    pt = (int(pt_temp[0]) , int(pt_temp[1]))
    return pt
  except:
    return None
    
def is_rectangle(coordinates):
  if len(coordinates) < 4:
    return False
  points = []
  for coord in coordinates:
      tempPt = getPoint(coord)
      if tempPt is None:
        return False
      points.append(tempPt)
  i = 0
  if is_midpt_90_deg(points[i],points[i+1],points[i+2]) \
    and is_midpt_90_deg(points[i+1],points[i+2],points[i+3]) \
    and is_midpt_90_deg(points[i+2],points[i+3],points[i]):
      return True
  return False

