"""


Let there be a square matrix, where each square is a rectangle, and a
combination of more squares are also rectangles. To find the number of
rectangles, Pete sat down and started counting... but that's highly
inefficient.

Create a function that takes the order of the matrix as input and returns the
number of rectangles in them.

### Examples

    rectangles(1) ➞ 1
    
    rectangles(2) ➞ 9
    
    rectangles(3) ➞ 36

### Notes

  * The input will always be an integer.
  * Number of rectangles are given by: `((n(n+1))/2)^2`
  * Watch the video listed in the **Resources** tab to get three different formulas.

"""

def rectangles(steps):
    return ((steps+1)*steps//2)**2

