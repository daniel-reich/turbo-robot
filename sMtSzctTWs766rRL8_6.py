"""


You will be implementing a basic case of the map-reduce pattern in
programming. Given a vector stored as a list of integers, find the magnitude
of the vector. Use the standard distance formula for n-dimensional Cartesian
coordinates.

### Examples

    magnitude([3, 4]) ➞ 5
    
    magnitude([0, 0, -10]) ➞ 10
    
    magnitude([]) ➞ 0
    
    magnitude([2, 3, 6, 1, 8] ) ➞ 10.677078252031311

### Notes

  * The list can have any length.
  * The input list will contain integers (except for empty list `[] ➞ 0`).

"""

from operator import *
from functools import *
def magnitude(lst):
  return reduce(add, map(lambda x: x*x, lst), 0)**0.5

