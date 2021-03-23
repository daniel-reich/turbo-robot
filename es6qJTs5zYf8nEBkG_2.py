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

def dup(n):
  for i,j in enumerate(n):
    for k,l in enumerate(n):
      if i!=k:
        if j==l:
          return True
  return False
def is_rectangle(coordinates):
  l=[]
  for i in coordinates:
    x=i.split(',')
    x[0]=int(x[0][1:])
    x[1]=int(x[1][:-1])
    l.append(x)
  if len(l)!=4:
    return False
  x1,x2,y1,y2=0,0,0,0
  for n1,i in enumerate(l):
    for n2,j in enumerate(l):
      if n1!=n2 and not dup(l):
        if i[0]==j[0]:
          if x1==0:
            x1=1
          else:
            x2=1
        if i[1]==j[1]:
          if y1==0:
            y1=1
          else:
            y2=1
  if x1 and x2 and y1 and y2:
    return True
  return False

