"""


Create a function that converts two lists of **x-** and **y-** coordinates
into a list of `(x, y)` coordinates.

### Examples

    convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) 
    ➞ [[1, 5], [5, 8], [3, 9], [3, 1], [4, 0]]
    
    convert_cartesian([9, 8, 3], [1, 1, 1]) 
    ➞ [[9, 1], [8, 1], [3, 1]]

### Notes

  * Each coordinate is a **list** , not a tuple.
  * `x` and `y` arrays will always be the same length.

"""

convert_cartesian=lambda x,y:[[i,j]for i,j in zip(x,y)]

