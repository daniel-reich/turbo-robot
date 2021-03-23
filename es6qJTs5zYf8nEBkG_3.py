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

def is_rectangle(coordinates):
  from ast import literal_eval
  #-----cell is just used for making rectangles-----#
  if len(coordinates) != 4:
    return False
  rectangle = coordinates
    
  #-----converts from str to tuples-----#
  rectangle = [literal_eval(i) for i in rectangle]
  rectangle = [list(i) for i in rectangle]
  
  #-----making the coords into usable variables-----#
  (ax, ay), (bx, by), (cx, cy), (dx, dy) = rectangle
  xAxis= [ax, bx, cx, dx]
  yAxis= [ay, by, cy, dy]
  xAxis.sort()
  yAxis.sort()
  
  #-----setting up variables to be referenced at end-----#
  xPairs = False
  yPairs = False
  
  #-----checking if there are two pairs of x and y values in rectangle-----#
  if xAxis[0] == xAxis[1]:
    xAxis.reverse()
    if xAxis[0] == xAxis[1]:
      xPairs = True
  if yAxis[0] == yAxis[1]:
    yAxis.reverse()
    if yAxis[0] == yAxis[1]:
      yPairs = True
    
  #-----checking if True-----#
  if xPairs and yPairs == True:
    return True
  else:
    return False

