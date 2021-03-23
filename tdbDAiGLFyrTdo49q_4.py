"""


Create a program that will take two lists of integers, `a` and `b`. Each list
will consist of 3 positive integers, representing the dimensions of cuboids
`a` and `b`. Find the difference of the cuboids' volumes.

For example, if the parameters passed are (`[2, 2, 3]`, `[5, 4, 1]`), the
volume of `a` is `12` and the volume of `b` is `20`. Therefore, the function
should return `8`.

### Examples

    find_difference([ 28, 16, 29 ], [ 7, 8, 17 ]) ➞ 12040
    
    find_difference([ 9, 22, 18 ], [ 16, 24, 10 ]) ➞ 276
    
    find_difference([ 1, 9, 25 ], [ 10, 7, 9 ]) ➞ 405
    
    find_difference([ 7, 6, 16 ], [ 26, 9, 26 ]) ➞ 5412

### Notes

Each list element is greater than 0.

"""

import numpy
def find_difference(a, b):
  return abs(numpy.prod(a) - numpy.prod(b))

