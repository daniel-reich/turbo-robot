"""


Create a function that takes the height and radius of a cone as arguments and
returns the volume of the cone rounded to the nearest hundredth. See the
resources tab for the formula.

![Volume of a Cone Image](https://edabit-
challenges.s3.amazonaws.com/volume_of_cone.gif)

### Examples

    cone_volume(3, 2) ➞ 12.57
    
    cone_volume(15, 6) ➞ 565.49
    
    cone_volume(18, 0) ➞ 0

### Notes

  * Return approximate answer by rounding the answer to the nearest hundredth.
  * Use Python's `math.pi` constant or equivalent, don't fall for 3.14 ;-)
  * If the cone has no volume, return `0`.

"""

def cone_volume(h, r):
  volume = 3.141592653589793*r**2*h/3
  x = round(volume, 2)
  return x

