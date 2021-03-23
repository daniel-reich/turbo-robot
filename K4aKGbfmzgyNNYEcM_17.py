"""


Given the _number_ `n` and a _list of interior angles_ `angles`, return
whether or not it's possible to make a convex polygon with `n` sides with the
`angles` given. Remember that angles must be **under 180°**.

    is_shape_possible(3, [80, 70, 30]) ➞ True

![Triangle with the angles 80, 70 and 30](https://edabit-
challenges.s3.amazonaws.com/interior-angles-triangle.png)

A shape with **3** sides and the angles **80°, 70° and 30°** is a possible
shape.

### Examples

    is_shape_possible(4, [90, 90, 90, 90]) ➞ True
    
    is_shape_possible(3, [20, 20, 140]) ➞ True
    
    is_shape_possible(1, [21]) ➞ False
    # n must be larger than 2
    
    is_shape_possible(5, [500, 10, 10, 10, 10]) ➞ False
    # You can't have an interior angle bigger than 180°

### Notes

  * Return `False` if `n` is less than 3 (see example #3).
  * There will always be an `n` number of positive integers given as `angles`.
  * The sum of interior angles is **(n - 2) x 180°**.

"""

def is_shape_possible(n, ang):
  return sum(ang)==(n-2)*180 and all(a<=180 for a in ang)

