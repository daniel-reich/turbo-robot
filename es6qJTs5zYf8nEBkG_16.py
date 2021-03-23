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
    if len(coordinates) != 4 or len(removeDuplicates(coordinates)) != 4:
        return False
    
    flag = 1
    for elem in coordinates:
        lst = coordinates
        coords = elem.split(",")
        lst.remove(elem)
        for i in lst:
            if str(coords[0]) in i and str(coords[0]) in i:
                flag = 0
​
    if flag == 1:
        return  False
    return True 
​
​
def removeDuplicates(txt):
    letters = []
    [letters.append(l) for l in txt if l not in letters]
    return letters

