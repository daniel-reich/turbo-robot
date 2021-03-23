"""


Imagine a circle and two squares: a smaller and a bigger one. For the smaller
one, the circle is a circumcircle and for the bigger one, an incircle.

![Scale](https://edabit-challenges.s3.amazonaws.com/scale.png)

Create a function, that takes an integer (radius of the circle) and returns
the difference of the areas of the two squares.

### Examples

    square_areas_difference(5) ➞ 50
    
    square_areas_difference(6) ➞ 72
    
    square_areas_difference(7) ➞ 98

### Notes

Use only positive integer parameters.

"""

def square_areas_difference(r):
  # big square:
    length_big_square = 2 * r
    area_big_square = (2 * r)  ** 2
    
    # small square:
    # r is the half diagonal of the small square!
    # corresponding Pythagoras:  r**2 + r**2 = length_small_square**2
    # That's the area of the small square too
    area_small_square = r**2 + r**2
    
    # Difference big - small square:
    return area_big_square - area_small_square

