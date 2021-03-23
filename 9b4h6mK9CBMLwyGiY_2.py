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

def get_distance(a, b):
   t= (a.get("x")- b.get("x"))**2
   v= (a.get("y")- b.get("y")) **2
   return round( (t+v)**(1/2), 3 )
   
   
   
print(get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16}))

