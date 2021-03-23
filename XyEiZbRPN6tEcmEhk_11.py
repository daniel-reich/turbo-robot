"""


Create a function that takes the length of the side of an equilateral triangle
in centimeters and returns the height of the triangle in millimeters.

### Examples

    height(2) ➞ 17.3 mm
    
    height(5) ➞ 43.3 mm
    
    height(6.2) ➞ 53.7 mm

### Notes

Return the answer rounded to one decimal place and in the format shown in the
examples above.

"""

def height(side):
  h = side * (3 ** .5) / 2
  return str(round((h * 10), 1)) + ' mm'
