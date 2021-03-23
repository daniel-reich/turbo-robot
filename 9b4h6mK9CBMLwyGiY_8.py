"""


In this challenge, you have to find the distance between two points placed on
a Cartesian plane. Knowing the coordinates of both the points, you have to
apply the **Pythagorean theorem** to find the distance between them.

![Two points on a Cartesian plane](https://edabit-
challenges.s3.amazonaws.com/coordinateplane26.png)

Given two dictionaries `a` and `b` being the two points coordinates ( **x**
and **y** ), implement a function that returns the distance between the
points, rounded to the nearest thousandth.

### Examples

    get_distance({"x": -2, "y": 1}, {"x": 4, "y": 3}) ➞ 6.325
    
    get_distance({"x": 0, "y": 0}, {"x": 1, "y": 1}) ➞ 1.414
    
    get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16}) ➞ 21.095

### Notes

  * Take a look at the **Resources** tab if you need a refresher on the geometry related to this challenge.
  * The "distance" is the shortest distance between the two points, or the straight line generated from `a` to `b`.

"""

from math import sqrt
def get_distance(a, b):
  a = str(a)
  t1 = a.find(':')
  t2 = a.find(',')
  t3 = a.rfind(':')
  t4 = a.find('}')
  x1 = int(a[t1+1:t2])
  y1 = int(a[t3+1:t4])
  b = str(b)
  t1 = b.find(':')
  t2 = b.find(',')
  t3 = b.rfind(':')
  t4 = b.find('}')
  x2 = int(b[t1+1:t2])
  y2 = int(b[t3+1:t4])
  r = sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
  return(round(r,3))

