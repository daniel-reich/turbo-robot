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

from collections import Counter
def is_rectangle(n):
  c=list()
  if(len(Counter(n))!=4):
    return False  
  for i in n:
    i=i.replace(" ","")
    i=i.split(",")
    print(i)
    c.append([int(i[0][1:]),int(i[1][0:len(i[1])-1])])
​
  dis=list()
  for i in range(0,len(c)):
    for j in range(i+1,len(c)):
      dis.append(abs(c[j][1]-c[i][1])+abs(c[j][0]-c[i][0]))
  dis=Counter(dis)
  print(dis)
  if(len(dis)>3):
    return False
  else:
    return True

