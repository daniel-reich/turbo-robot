"""


Every quadratic curve `y = a x² + b x + c` has a **vertex** point: the turning
point where the curve stops heading down and starts going up.

Given the values `a`, `b` and `c`, you need to return the coordinates of the
vertex. Return your answers rounded to 2 decimal places.

### Examples

    find_vertex(1, 0, 25)  ➞ [0, 25]
    # The vertex of y=x²+25 is at (0, 25).
    
    find_vertex(-1, 0, 25) ➞ [0, 25]
    # The vertex of y=-x²+25 is at (0, 25).
    
    find_vertex(1, 10, 4) ➞ [-5, -21]
    # The vertex of y=x²+10x+4 is at (-5, -21).

### Notes

  * See **Resources** if you're not sure how to find the x or y coordinates of the vertex.
  * `a` will always be non-zero.

"""

def find_vertex(a, b, c):
  x = -b/(2*a)
  return [x, a*(x**2)+b*x+c]

