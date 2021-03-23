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

def euclid_d2(cor1, cor2):
  if len(cor1)!=len(cor2): return(False)
  else: return(sum([(cor2[i]-cor1[i])**2 for i in range(len(cor1))]))
​
def check_orthg(cor1,cor2,cor3):
  distances=set([euclid_d2(cor1,cor2),euclid_d2(cor1,cor3),euclid_d2(cor2,cor3)])
  diag=max(distances)
  distances.remove(diag)
  if diag==sum(distances): return(True)
  else: return(False)
  
def is_rectangle(coordinates):
  if len(coordinates)!=4: return(False)
  coords=[eval(l) for l in coordinates]
  return(check_orthg(coords[0],coords[1],coords[2]) 
         and check_orthg(coords[0],coords[1],coords[3])  
         and check_orthg(coords[0],coords[2],coords[3]))

